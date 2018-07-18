# 1. Dev-env, super-easy mode (docker all things)

Requirements:
- [Install docker](https://docs.docker.com/install/)
- Learn [Python](https://docs.python.org/3/tutorial/) and [Django](https://docs.djangoproject.com/en/2.0/intro/tutorial01/)
- Learn [vue.js](https://vuejs.org/)
- Learn [Nuxt.js](https://nuxtjs.org/)
- Get familiar with [Vuetify.js](https://vuetifyjs.com/en/) components

Step by step

```bash
source dev.sh  # import useful bash functions
devhelp  # like this one ;)
dkbuild  # builds the docker image for this project. The first time Will take a while.
dknpminstall  # I'll explain later!
dkup  # Brings up everything
```

With `dkup` running, open another terminal

```bash
dk bash  # starts bash inside "djavue-twitter" container
./manage.py migrate  # create database tables and stuff
./manage.py createsuperuser  # creates an application user in the database
```

What is happenning:

* `dev.sh` is a collection of useful bash functions for this project's development environment. You're encouraged to look inside and see how that works, and add more as the project progresses.
* `dknpminstall` will start a docker container and run `npm install` inside to download node dependencies to the `frontend/node_modules` folder. Using docker for this means you don't need to worry about installing (and choosing version for) node/npm.
* `dkup` uses docker-compose to start 3 containers: postgres, nginx, and djavue-twitter.
* The dockerized postgres saves its state into `docker/dkdata`. You can delete that if you want your dev database to go kaboom.
* Once `dkup` is running, `dk <command>` will run `<command>` inside the `djavue-twitter` container. So `dk bash` will get you "logged in" as root inside that container. Once inside, you need to run Django's `manage.py` commands to initialize the database properly.
* The djavue-twitter container runs 3 services:
 * django on port 8000
 * nuxt frontend with real APIs on port 3000
 * nuxt frontend with mock APIs on port 3001
* nginx is configured to listen on port 80 and redirect to 8000 (requests going to `/api/*`) or 3000 (everything else).
* Therefore, when `dkup` is running, you get a fully working dev-environment by pointing your browser to http://localhost, and a frontend-only-mock-api-based environment by pointing your browser to http://localhost:3001. Each one is more useful on different situations.
* You're supposed to create features first by implementing them on 3001, then validate them, and only then write the backend APIs and integrate them. Experience shows this process is very productive.

# 2. Dev-env, normal-easy mode (dockerize nginx + postgres)

Running everything inside docker is a quick and easy way to get started, but sometimes we need to run things "for real", for example, when you need to debug python code.

## Python setup

Requirements:
 - Python3, check if you have the python 3.6. If you don't, you can install doing the following:
 ```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.6 libpython3.6-dev python3-dev
sudo apt install python-pip
python -m pip install --user --upgrade pip==9.0.3
```
 - Understand about python [virtualenvs](https://docs.python.org/3/tutorial/venv.html)
 - Install [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/), after installation run:
 ```
 mkdir -p ~/Envs
 ```
 - Make sure you have added to your .bashrc file the following
 ```
source $HOME/.local/bin/virtualenvwrapper.sh
export WORKON_HOME=~/Envs
```

Step by step

```bash
dkpgnginx  # Starts postgres and nginx inside docker
```

With `dkpgnginx` running, start another terminal:

```bash
mkvirtualenv djavue-twitter -p python3.6  # creates a python3 virtualenv
pip install -r requirements.txt  # install python dependencies inside virtualenv
export DJANGO_DB_PORT=5431  # That's where our dockerized postgres is listening
./manage.py runserver  # starts django on port 8000
```

Since nginx is also running you go ahead and point your browser to http://localhost/admin and you should see the same thing as in http://localhost:8000/admin

## Node Setup

Requirements:

* Install [nvm](https://github.com/creationix/nvm) (not required, but highly recommended)

Step by step:

```bash
nvm use 9  # Switch your terminal for node version 9.x
# no need to npm install anything, we already have our node_modules folder
sudo chmod -R o+rw .nuxt/  # I'll explain this later
npm run dev  # Starts nuxt frontend on port 3000
```

You can go ahed and point your browser to http://localhost:3000 to see nuxt running **with mocked apis**

To run nuxt using real APIs just turn set this environment variable API_MOCK=0

```bash
API_MOCK=0 npm run dev  # Starts nuxt frontend on port 3000
```

Since nginx is also running you go ahead and point your browser to http://localhost/ and you should have a fully integrated frontend+backend dev env.

# 3. Helpers
* vue command
```
npm install -g vue-cli
```
* mkpasswd command
```
sudo apt install whois
```

# 4. EC2 instance
* Get your EC2 instance, download the pem
* Add role to allow the instance to access RDS
* Give the right permission to your pem
```
chmod 600 <your>.pem
```
* ssh to it and add your public key to it so you don't need aws pem to ssh anymore
* Add swap to the machine. Tou can just run [this commands](https://github.com/tonylampada/randomstuff/blob/gh-pages/swap_digitalocean.sh) or c the [Digital Ocean tutorial] or (https://www.digitalocean.com/community/tutorials/how-to-add-swap-space-on-ubuntu-16-04)
* [Install docker and configuration](https://github.com/tonylampada/randomstuff/blob/gh-pages/install_docker_ubuntu.md)
* Add docker prune to crontab - https://github.com/tonylampada/randomstuff/blob/gh-pages/docker_prune.sh
```
mkdir ~/cron
vim ~/cron/docker_prune.sh
chmod +x ~/cron/docker_prune.sh
crontab -e
# 0 0 * * * /home/ubuntu/cron/docker_prune.sh
```
* Here you can create a AMI so you don't need to repeat this setup again
* Install nginx and git
```
sudo apt-get install nginx git
```
* If you check the ec2 public dns you will see the nginx page
* clone the repo
* build the docker machine dkbuild
* Create RDS instance
* test connecting mysqlworkbench
* Save the database password in an env file as well as database name, database DNS
```
DJANGO_DB_NAME=mamae
DJANGO_DB_USER=mamae
DJANGO_DB_HOST=mamae.cmxj48itgyn5.us-east-1.rds.amazonaws.com
DJANGO_DB_PASSWORD=mamae
DJANGO_DEBUG=0
```
* configure nginx
```
server {
    listen       80;
    server_name  davidjgluckman.com;

    location /api {
        proxy_pass http://localhost:8000/api;
    }
    location /admin {
        proxy_pass http://localhost:8000/admin;
    }
    location /static {
	alias /home/ubuntu/dkdata/djavue-twitter/static;
    }
    location / {
        proxy_pass http://localhost:3000/;
    }
}
```
* reload nginx
* configure /etc/host for your domain
* run the docker
* Add HTTPS - https://github.com/tonylampada/randomstuff/blob/gh-pages/letsencrypt_certbot.sh
As root add to cron tab
0 0 1 3,6,9,12 certbot renew
* HTTPS with ALB + Nginx - https://www.youtube.com/watch?v=Dq9_U0bFffg
* Connection draining - https://aws.amazon.com/blogs/aws/elb-connection-draining-remove-instances-from-service-with-care/
* ALB health check - Nginx config - https://codyparker.com/force-entire-site-ssl-nginx-behind-aws-load-balancer/

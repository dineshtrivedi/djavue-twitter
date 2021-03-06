import Vue from 'vue'

var logged_user = null;

function mockasync (data) {
  return new Promise((resolve, reject) => {
    setTimeout(() => resolve({data: data}), 600)
  })
}

const api = {
    login(username, password){
        if(password){
            logged_user = {
                username: username,
                first_name: 'Mark',
                last_name: 'Zuckerberg',
                email: 'zuck@facebook.com',
                notifications_enabled: true,
                permissions:{
                    ADMIN: username == 'admin',
                    STAFF: username == 'admin',
                }
            };
        }
        return mockasync(logged_user);
    },
    logout(){
        logged_user = null;
        return mockasync({});
    },
    whoami(){
        return mockasync(logged_user ? {
            authenticated: true,
            user: logged_user,
        } : {authenticated: false});
    },
    add_todo(newtask){
        return mockasync({description: newtask, done: false});
    },
    list_todos(){
        return mockasync({
            todos: [
                {description: 'Do the laundry', done: true},
                {description: 'Walk the dog', done: false}
            ]
        });
    },
    list_tweets(username){
        const d = new Date()
        const _1min = 60000;
        const _1h = 60 * _1min;
        const d1 = new Date(d.getTime() - 15 * _1min)
        const d2 = new Date(d.getTime() - 2 * _1h)

        return mockasync([
            {
                id: 1,
                author_name: 'Jose da Silva',
                author_username: username || '@jsilva',
                author_avatar: "https://cloud.netlifyusercontent.com/assets/344dbf88-fdf9-42bb-adb4-46f01eedd629/242ce817-97a3-48fe-9acd-b1bf97930b01/09-posterization-opt.jpg",
                created_at: d.toISOString(),
                text: "Where is the coffee?"
            },
            {
                id: 2,
                author_name: 'Paul Mersacik',
                author_username: username || '@pmersacik',
                author_avatar: "https://demo.phpgang.com/crop-images/demo_files/pool.jpg",
                created_at: d1.toISOString(),
                text: "Where is the coffee?[2]"
            },
            {
                id: 3,
                author_name: 'Tinashe T.',
                author_username: username ||  '@tinashe',
                author_avatar: "https://i.kinja-img.com/gawker-media/image/upload/t_original/bhjivrw2chm9um9yrrmy.jpg",
                created_at: d2.toISOString(),
                text: "Where is the coffee?[3]"
            },
          ])
    },
    get_user_details(username) {
        const avatar = {
            '@jsilva': "https://cloud.netlifyusercontent.com/assets/344dbf88-fdf9-42bb-adb4-46f01eedd629/242ce817-97a3-48fe-9acd-b1bf97930b01/09-posterization-opt.jpg",
            '@pmersacik': "https://demo.phpgang.com/crop-images/demo_files/pool.jpg",
            '@tinashe': "https://i.kinja-img.com/gawker-media/image/upload/t_original/bhjivrw2chm9um9yrrmy.jpg"
        }[username];

        return mockasync({
            username: username,
            avatar: avatar,
            last_tweet: "I think therefore I am",
            iFollow: true
        })
    },
    follow(username) {
        return mockasync({})
    },
    unfollow(username) {
        return mockasync({})
    },
    tweet(text) {
        const d = new Date()
        return mockasync({
            id: 1000,
            author_name: logged_user.username,
            author_username: logged_user.username,
            author_avatar: "https://cloud.netlifyusercontent.com/assets/344dbf88-fdf9-42bb-adb4-46f01eedd629/242ce817-97a3-48fe-9acd-b1bf97930b01/09-posterization-opt.jpg",
            created_at: d.toISOString(),
            text: text
        })
    }
};

export default api;

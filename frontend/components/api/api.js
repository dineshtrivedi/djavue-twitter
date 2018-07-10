import axios from '~/helpers/axios';

axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = "csrftoken";

const api = {
    login(username, password){
        return post('/api/login', {username: username, password: password});
    },
    logout(){
        return post('/api/logout');
    },
    whoami(){
        return get('/api/whoami');
    },
    add_todo(newtask){
        return post('/api/add_todo', {new_task: newtask});
    },
    list_todos(){
        return get('/api/list_todos');
    },
    list_tweets(username){
        return get('/api/list_tweets', {username: username});
    },
    get_user_details(username) {
        return get('/api/get_user_details', {username: username});
    },
    follow(username) {
        return post('/api/follow', {username: username});
    },
    unfollow(username) {
        return post('/api/unfollow', {username: username});
    },
    tweet(text) {
        return post('/api/tweet', {text: text})
    }
}
export default api;

function get(url, params){
    return axios.get(url, {params: params});
}

function post(url, params){
    var fd = new FormData();
    params = params || {}
    Object.keys(params).map((k) => {
        fd.append(k, params[k]);
    })
    return axios.post(url, fd);
}

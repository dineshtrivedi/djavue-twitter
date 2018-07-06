<template>
    <viewuser :tweets="tweets" :user="user"></viewuser>
</template>

<script>
import viewuser from '~/components/ViewUser.vue'
import AppApi from '~apijs'

export default {
    components: {
        viewuser: viewuser
    },
    asyncData(context) {
        const username = context.params.username;
        const p1 = AppApi.get_user_details(username);
        const p2 = AppApi.list_tweets();

        return Promise.all([p1, p2]).then(r => {
            return {
                user: r[0].data,
                tweets: r[1].data,
            }
        })
    },
    data() {
        return {
            tweets: [],
        }
    }
}
</script>

<style>
</style>

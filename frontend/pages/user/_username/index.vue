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
        return AppApi.list_tweets().then(r => {
            return {
                tweets: r.data,
                user: {
                    username: username
                }
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

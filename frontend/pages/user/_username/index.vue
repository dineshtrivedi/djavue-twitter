<template>
    <h1>This is a user timeline - {{username}}</h1>
</template>

<script>

export default {
    asyncData(context) {
        return {
            username: context.params.username
        }
    },
    data() {
        return {}
    }
}
</script>

<style>
</style>

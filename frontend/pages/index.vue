<template>
  <div>
    <home :tweets="tweets" ></home>
    <v-progress-linear v-if="!tweets" :indeterminate="true"></v-progress-linear>
  </div>
</template>

<script>

import home from '~/components/home.vue'
import AppApi from '~apijs'

export default {
  components: {
    home
  },
  data () {
    return {}
  },
  asyncData() {
    return AppApi.list_tweets().then(r => {
      return {
        tweets: r.data
      }
    })
  }
}
</script>

<style>
</style>

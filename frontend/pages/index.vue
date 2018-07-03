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
    home: home
  },
  data () {
    return {
      tweets: null,
    }
  },
  mounted() {
    // const self = this
    AppApi.list_tweets().then(result => {
      this.tweets = result.data
    })
  }
}
</script>

<style>
</style>

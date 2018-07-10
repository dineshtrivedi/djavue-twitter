<template>
  <div>
    <newtweet @newtweet="addToTimeline($event)"></newtweet>
    <timeline :tweets="tweets"></timeline>
  </div>
</template>

<script>

import timeline from '~/components/timeline.vue'
import newtweet from '~/components/NewTweet.vue'

export default {
  props: ['tweets'],
  components: {
    timeline,
    newtweet
  },
  data () {
    return {}
  },
  methods: {
    addToTimeline(event){
      const tweet = event.data
      this.tweets.push(tweet)
    }
  }
}
</script>

<style>
</style>

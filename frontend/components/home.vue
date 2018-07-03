<template>
  <timeline :tweets="tweets"></timeline>
</template>

<script>

import timeline from '~/components/timeline.vue'

export default {
  props: ['tweets'],
  components: {
    timeline: timeline
  },
  data () {
    return {}
  }
}
</script>

<style>
</style>

<template>
  <home :tweets="tweets"></home>
</template>

<script>

import home from '~/components/home.vue'
export default {
  components: {
    home: home
  },
  data () {
    return {
      tweets: [
        {
            id: 1,
            author_name: 'Jose da Silva',
            author_username: '@jsilva',
            author_avatar: "https://cloud.netlifyusercontent.com/assets/344dbf88-fdf9-42bb-adb4-46f01eedd629/242ce817-97a3-48fe-9acd-b1bf97930b01/09-posterization-opt.jpg",
            created_at: '43m',
            text: "Where is the coffee?"
        },
        {
            id: 2,
            author_name: 'Paul Mersacik',
            author_username: '@pmersacik',
            author_avatar: "https://demo.phpgang.com/crop-images/demo_files/pool.jpg",
            created_at: '52m',
            text: "Where is the coffee?[2]"
        },
        {
            id: 3,
            author_name: 'Tinashe T.',
            author_username: '@tinashe',
            author_avatar: "https://i.kinja-img.com/gawker-media/image/upload/t_original/bhjivrw2chm9um9yrrmy.jpg",
            created_at: '59m',
            text: "Where is the coffee?[3]"
        },
      ]
    }
  }
}
</script>

<style>
</style>

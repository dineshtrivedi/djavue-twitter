<template>
    <v-card color="cyan darken-2" class="white--text">
        <v-container fluid grid-list-lg>
        <v-layout row>
            <v-flex xs7>
            <div>
                <div class="headline">{{user.username}}</div>
                <div>{{user.last_tweet}}</div>
            </div>
            </v-flex>
            <v-flex xs5>
                <v-avatar
                    :size="125"
                    color="grey lighten-4">
                    <img :src="user.avatar" alt="avatar">
                </v-avatar>
                <div v-if="logged_user">
                    <v-btn v-if="!user.iFollow" :loading="loading" block color="success" @click="follow()">Follow</v-btn>
                    <v-btn v-if="user.iFollow" :loading="loading" block color="error" @click="unfollow()">Unfollow</v-btn>
                </div>
            </v-flex>
        </v-layout>
        </v-container>
    </v-card>
</template>

<script>
import AppApi from '~apijs'
import Snacks from '~/helpers/Snacks.js'

export default {
    props: ['user'],
    data() {
        return {
            loading: false,
        }
    },
    computed: {
        logged_user() {
            return this.$store.getters.logged_user
        }
    },
    methods: {
        follow(){
            this.loading = true;
            AppApi.follow(this.user.username).then(() => {
                this.user.iFollow = true
                this.loading = false

                Snacks.show(this.$store, {
                    text: "You are now following " +  this.user.username
                })
            })
        },
        unfollow() {
            this.loading = true;
            AppApi.unfollow(this.user.username).then(() => {
                this.user.iFollow = false
                this.loading = false;
                Snacks.show(this.$store, {
                    text: "You have unfollowed " +  this.user.username,
                    color: "error",
                    timeout: 3000
                })
            })
        }
    }
}
</script>

<style>
</style>

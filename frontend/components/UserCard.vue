<template>
    <!-- <h1>{{user.username}}</h1> -->
    <v-flex xs12>
        <v-card color="cyan darken-2" class="white--text">
            <v-container fluid grid-list-lg>
            <v-layout row>
                <v-flex xs7>
                <div>
                    <div class="headline">{{user.username}}</div>
                    <div>Foster the People</div>
                </div>
                </v-flex>
                <v-flex xs5>
                    <v-avatar
                        :size="125"
                        color="grey lighten-4">
                        <img src="https://demo.phpgang.com/crop-images/demo_files/pool.jpg" alt="avatar">
                    </v-avatar>
                </v-flex>
            </v-layout>
            </v-container>
        </v-card>
    </v-flex>
</template>

<script>
export default {
    props: ['user'],
    data() {
        return {}
    }
}
</script>

<style>
</style>

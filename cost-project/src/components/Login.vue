<template>
    <div class="login">
        <form @submit.prevent="user_stor.auth_user(login,password,router)" action="">
            <div class="form_block">
                <img class="man_img" src="../assets/login/man.png" alt="">
                <div class="form_block_items">
                    <input type="text" placeholder="Login" v-model="login">
                </div>
                <div class="form_block_items">
                    <input type="password" placeholder="Password" v-model="password">
                </div>
                <div class="form_block_submit">
                    <input type="submit" value="Login in">
                </div>
                <div class="form_block_register_link">
                    <router-link to="/register">Do not register?</router-link>
                </div>
                <img class="form_img" src="../assets/login/online-survey.png" alt="">
            </div>
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { user_store } from '../store/user_store';
import { useRouter } from 'vue-router';
let user_stor = user_store()
let router = useRouter()

 let login = ref('')
 let password = ref('')
</script>

<style>

</style>
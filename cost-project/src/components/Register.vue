<template>
    <div class="login">
        <form @submit.prevent="user_storage.register_user(login,password,confirm_password,email,phone,router)" action="">
            <div class="form_block">
                <img class="man_img" src="../assets/login/man.png" alt="">
                <div class="form_block_items">
                    <input type="text" placeholder="Login" v-model="login">
                </div>
                <div class="form_block_items">
                    <input type="password" placeholder="Password" v-model="password">
                </div>
                <div class="form_block_items">
                    <input type="password" placeholder="Confirm password" v-model="confirm_password">
                </div>
                <div class="form_block_items">
                    <input type="email" placeholder="Email" v-model="email">
                </div>
                <div class="form_block_items">
                    <input type="text" placeholder="Phone number" v-model="phone">
                </div>
                <div class="form_block_submit">
                    <input type="submit" value="Register">
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

const router = useRouter()
 let login = ref('')
 let password = ref('')
 let confirm_password = ref('')
 let email = ref('')
 let phone = ref('')
//Create store
let user_storage = user_store()

</script>

<style>

</style>    
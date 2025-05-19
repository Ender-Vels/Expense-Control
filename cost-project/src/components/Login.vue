<template>
    <div class="login">
        <form @submit.prevent="LoginIn">
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
let userStore = user_store()
let router = useRouter()

 let login = ref('')
 let password = ref('')


 async function LoginIn() {
    if(login.value.length<4){
        alert("Login must have 4 or more symbols")
    }
    else if(password.value.length<6){
        alert("Password must have 5 or more symbols")
    }
    else{
        let data={
            login:login.value,
            password: password.value
        }
        await userStore.auth_user(data,router)
    }
 }


</script>

<style>

</style>
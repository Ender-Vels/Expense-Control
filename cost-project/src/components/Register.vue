<template>
    <div class="login">
        <form @submit.prevent="register">
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
                    <input type="text" placeholder="Phone number" v-model="phone" maxlength="10">
                </div>
                <div class="form_block_submit">
                    <input type="submit" value="Register">
                </div>
                <div class="form_block_register_link">
                    <router-link to="/login">You have Account?</router-link>
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
let userStore = user_store()




async function register() {
    if(password.value.length<6){
        alert("Password length must be 6 symbols minimum")
    }
    else if(password.value != confirm_password.value){
        alert("Password and Confirm password do not match")
    }
    else{
        let data={
            login: login.value,
            password: password.value,
            email: email.value,
            phone:phone.value
        }
        await userStore.register_user(data,router)
    }
}
</script>

<style>

</style>    
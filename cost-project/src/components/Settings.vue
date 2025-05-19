<template>
    <Header/>
    <div class="setting">
        <div class="setting_block">
            <!--Change login-->
            <div class="setting_change">
                <div class="setting_iput">
                    <input type="text" placeholder="New Login" v-model = "login">
                    <div class="setting_btn">
                        <button @click = "put_login">Change</button>
                    </div>
                </div>
                <div class="setting_description">
                    <span>Login must have 4 symbols</span>
                </div>
            </div>
            <!--Change email-->
            <div class="setting_change">
                <div class="setting_iput">
                    <form class="set_input" @submit.prevent="put_email">
                    <input type="email" placeholder="New Email" v-model = "email">
                    <div class="setting_btn">
                        <button type="submit">Change</button>
                    </div>
                    </form>
                </div>
                <div class="setting_description">
                    <span></span>
                </div>
            </div>
            <!--Change password-->
            <div class="setting_change">
                <div class="setting_iput_pass">
                    <input type="password" placeholder="Old Password" v-model = "old_pass">
                    <input type="password" placeholder="New Password" v-model = "new_pass">
                    <input type="password" placeholder="Confirm New Password" v-model = "confirm_pass">
                    
                    <div class="setting_btn">
                        <button @click = "put_password">Change</button>
                    </div>
                </div>
                <div class="setting_description">
                    <span>Password must have 6 symbols</span>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref,onMounted } from "vue";
import Header from "./Dashboard/Header.vue"
import { user_store } from "../store/user_store";

let userStore = user_store()



let login = ref('')
let email = ref('')
let old_pass = ref('')
let new_pass = ref('')
let confirm_pass = ref('')


async function put_email(){
    let ids = userStore.get_id
    if(email.value == ''){
        alert("Email form empty")
    }
    else{
        let data= {
            email:email.value,
            user_id: ids
        }
        await userStore.change_email(data)
        await userStore.refresh_token()
        email.value = ''
        window.location.reload()
    }

}

async function put_login(){
    let ids = userStore.get_id
    if(login.value == ''){
        alert("Login form empty")
    }
    else if(login.value.length<=4){
        alert("Login length must be minimum 4 symbols")
    }
    else{
        let data= {
            login:login.value,
            user_id: ids
        }
        await userStore.change_login(data)
        await userStore.refresh_token()
        login.value = ''
        window.location.reload()
    }

}

async function put_password(){
    let ids = userStore.get_id
    if(new_pass.value != confirm_pass.value){
        alert("New password and Confirm Password do not mutch")
    }
    else if(new_pass.value.length<=6){
        alert("Password must have minimum 6 symbols")
    }
    else{
        let data= {
            user_id: ids,
            old_pass: old_pass.value,
            new_pass: new_pass.value
            
        }
        await userStore.change_password(data)
        await userStore.refresh_token()
        old_pass.value =''
        new_pass.value = ''
        confirm_pass.value = ''
        window.location.reload()
    }

}






onMounted(async()=>{
    userStore.refresh_token()
})

</script>
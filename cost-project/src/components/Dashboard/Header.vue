<template>
        <PopUp/>
    <header>

        <div class="header">
            <div class="header_title">
                <div class="header_burger">
                    <button @click="open_side"><img src="../../assets/dash/setting-menu-burger-circle.256x256.png" alt=""></button>
                </div>
                <p>Cost control</p>
            </div>
            <div class="header_account" @click="acc_settings">
                <div class="header_account_icon">
                    <img src="../../assets/dash/user.png" alt="">
                </div>
                <div class="header_account_name">
                    <p>{{ user_storage.get_name }}</p>
              </div>
              <div class="header_account_sub" v-if="is_show_settings">
                        <ul class="account_settings"> 
                            <li><button @click="change_info">Setting</button></li>
                            <li><button @click="exit">Exit</button></li>
                        </ul>
                    </div>
            </div>
        </div>
    </header>
</template>

<script setup>

    
    import { user_store } from '../../store/user_store';
    import PopUp from './PopUp.vue'
    import { ref } from 'vue';
    import { useRouter } from 'vue-router'

    
    let user_storage = user_store()
    let is_show_settings = ref(false)
    let router = useRouter()


    function open_side(){
        let side = document.querySelector('.side')
        side.classList.add('active')
        setTimeout(()=>{
            let side_block = document.querySelector('.side_menu')
            side_block.classList.add('active')
        },200)
    }
    function  acc_settings(){
        is_show_settings.value = !is_show_settings.value
    }
    function exit(){
        user_storage.logout_user(router)
    }
    function change_info(){
        router.push('/setting')
        is_show_settings.value = !is_show_settings.value
    }

</script>

<style>

</style>


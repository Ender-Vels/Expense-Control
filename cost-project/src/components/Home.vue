<template>
    <div class="home">
        <!--UnAuth user-->
        <div class="home_auth">
            <img class="calc" src="../assets/calculator.png" alt="calc">
            <div class="home_greet">
                <h1>Cost Control</h1>

            </div>
            <div class="home_action">
                <router-link to="/login" class="start_btn">Get Start</router-link>
                <router-link class="about_btn">About Service</router-link>
            </div>
            <img class="note" src="../assets/sticky-notes.png" alt="calc">
        </div>
        <!---->


    </div>
</template>

<script setup>
    import {ref,onMounted} from 'vue'


    
</script>

<style>

</style>
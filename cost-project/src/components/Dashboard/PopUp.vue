<template>
    <div class="side" @click="close_side">
        <div class="side_menu">
            <div class="side_menu_title">
                <P>Dashboard Menu</P>
            </div>
            <ul class="side_menu_nav">
                <li class="side_menu_item">
                    <router-link to="/dashboard">Home <img src="../../assets/dash/—Pngtree—vector forward icon_4184777.png" alt=""></router-link> 
                </li>
                <li class="side_menu_item">
                    <router-link to="/income">Income <img src="../../assets/dash/—Pngtree—vector forward icon_4184777.png" alt=""></router-link> 
                </li>
                <li class="side_menu_item">
                    <router-link to="/expenses">Expenses <img src="../../assets/dash/—Pngtree—vector forward icon_4184777.png" alt=""></router-link> 
                </li>
            </ul>
        </div>
    </div>
</template>

<script setup>

function close_side(){
    let side = document.querySelector('.side')
    side.classList.remove('active')
    let side_block = document.querySelector('.side_menu')
    side_block.classList.remove('active')
}
</script>

<style>

</style>
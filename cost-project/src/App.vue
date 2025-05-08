<script setup>
  import {ref,onMounted} from 'vue'
  import { user_store } from './store/user_store';

  let user_storage = user_store()

  onMounted(()=>{
    user_storage.set_auth_status()
  })
</script>

<template>
  <div>

  </div>
  <router-view></router-view>
</template>

<style >

</style>

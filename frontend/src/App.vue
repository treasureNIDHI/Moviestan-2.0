<template>
  <div id="app">
    <NavBar></NavBar>
    <router-view/>
  </div>
</template>

<style>
@import'~bootstrap/dist/css/bootstrap.css';
</style>
<script>
import NavBar from '@/components/NavBar.vue'
export default {
  components:{
    NavBar,
  }
}
</script> 
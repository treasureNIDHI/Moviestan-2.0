<template>
<div><ul class="nav justify-content-center">
  <li class="nav-item">
    <router-link class="nav-link active" aria-current="page" to="/user/bookings">Your Bookings</router-link>
  </li>
  <li class="nav-item">
    <router-link class="nav-link" to="/user">Dashboard</router-link>
  </li>
  <li class="nav-item">
    <router-link class="nav-link" to="/user/profile">Profile</router-link>
  </li>
  
</ul>

<router-view/>
</div>
</template> 
<script>
export default{
    name:'UserView'
}
</script>
<style>
</style>
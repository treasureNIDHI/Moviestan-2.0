<template>
    <div><ul class="nav justify-content-center">
      <li class="nav-item">
        <router-link class="nav-link active" aria-current="page" to="/admin">Dashboard</router-link>
      </li>
      
      <li class="nav-item">
        <router-link class="nav-link" to="/admin/control">Control</router-link>
      </li>
      <li class="nav-item">
        <router-link class="nav-link" to="/admin/profile">Profile</router-link>
      </li>
      
      
    </ul>
    <router-view/>
    </div>
</template> 
<script>
    export default{
        name:'AdminView'
    }
</script>
<style>
</style>
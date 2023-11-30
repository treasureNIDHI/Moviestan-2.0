<template>
<div>
    <h1><center>My Profile</center></h1>
    <section class="container my-2 bg-dark w-50 text-light p-2">
        <form form @submit.prevent="update_profile()" method="POST" enctype="multipart/form-data" class="row g-3">
            <div class="col-md-4">
    <label for="validationCustom01"  class="form-label">First name</label>
    <input type="text" v-model="name" class="form-control" id="validationCustom01" value="Mark" required>
    <div class="valid-feedback">
      Looks good!
    </div>
  </div>

  <div class="col-md-6">
    <label for="inputEmail4"  class="form-label">Email</label>
    <input type="email" v-model="email" class="form-control" id="inputEmail4" disabled>
  </div>
  <div class="col-md-6">
    <label for="inputPassword4" class="form-label">Password</label>
    <input type="password" v-model="password" class="form-control" id="inputPassword4" required>
  </div>
  <div class="col-12">
    <label for="inputAddress" class="form-label">Address</label>
    <input type="text" v-model="address" class="form-control" id="inputAddress" placeholder="Chennai,TN">
  </div>
  <div class="col-12">
    <label for="inputAddress2" class="form-label">Contact Number</label>
    <input type="text" v-model="ph_nume" class="form-control" id="inputAddress2">
  </div>
  <!-- <div class="col-md-6">
    <label for="inputCity" class="form-label">City</label>
    <input type="text" class="form-control" id="inputCity">
  </div> -->
  <!-- <div class="col-md-4">
    <label for="inputState" class="form-label">State</label>
    <select id="inputState" class="form-select">
      <option selected>Choose...</option>
      <option>...</option>
    </select>
  </div> -->
  <!-- <div class="col-md-2">
    <label for="inputPIN" class="form-label">PIN</label>
    <input type="text" class="form-control" id="inputPIN">
  </div> -->

  <div class="col-12">
    <button type="submit" class="btn btn-primary">Save</button>
  </div>
</form>
    </section>
</div>
</template>

<script>
import { RouterLink } from 'vue-router';

export default {

  data() {
    return {
      isLoggedIn: false,
      name:"",
      email: "",
      password: "",
      repassword: "",
      ph_nume: "",
      address: ""
    };
  },

mounted(){
  fetch("http://127.0.0.1:8000/api/member", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
          Authorization: "Bearer " + localStorage.getItem("access_token")

        }
      })
      .then(res=>res.json())
      .then(data =>{
        this.name = data.Name,
        this.address = data.Address,
        this.ph_nume = data.ph_num,
        this.email=data.email_ID
        console.log(data);
      })
},


methods:{
update_profile() {
  const obj = {
        email: this.email,
        password: this.password,
        name: this.name,
        ph_nume: this.ph_nume,
        address: this.address,
      }; 


fetch(`http://127.0.0.1:8000/api/member`, {
  method: "PUT",
  headers: {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
    Authorization: "Bearer " + localStorage.getItem("access_token")
  },
  body: JSON.stringify(obj)
})
  .then(res => res.json())
  .then(data => {
    console.log(data);
    // this.updatedprofile=data
  })
  .catch(error => {
    console.error("Error:", error);
    
  });
}
},
}


</script>
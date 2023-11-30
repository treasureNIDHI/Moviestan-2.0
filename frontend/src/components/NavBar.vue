<template>
  <nav class="navbar navbar-expand-lg navbar-fixed-top bg-body-tertiary mt-3 ps-4">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Moviestan</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto ms-4 mb-2 mb-lg-0">
          <!-- <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Cities
            </a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">City1</a></li>
              <li><a class="dropdown-item" href="#">City2</a></li>
              <li>
                <hr class="dropdown-divider" />
              </li>
              <li><a class="dropdown-item" href="#">City3</a></li>
            </ul>
          </li> -->
          <!-- <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Ratings</a>
          </li> -->
        </ul>
        <form class="d-flex" role="search" @submit.prevent="search">
          <input class="form-control" type="search" placeholder="Search" aria-label="Search" v-model="searchstring" />
          <button class="btn btn-outline-success" type="submit" data-bs-toggle="modal" data-bs-target="#exampleModal">Search</button>
        </form>
        <!-- Modal -->
        <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <table id="Show">
                  <tr>
                    <th>ID &nbsp; &nbsp;</th>
                    <th>Name &nbsp; &nbsp;</th>
                    <th>Rating &nbsp; &nbsp;</th>
                    <th>Tags &nbsp; &nbsp;</th>
                    <th>Ticket_Price &nbsp; &nbsp;</th>
                    <th>Time &nbsp; &nbsp;</th>
                    <th>Book Show</th>
                  </tr>
                  <tr v-for="s in shows" :key="s.ID">
                    <td>{{ s.ID }}</td>
                    <td>{{ s.Name }}</td>
                    <td>{{ s.Rating }}</td>
                    <td>{{ s.Tags }}</td>
                    <td>{{ s.Ticket_Price }}</td>
                    <td>{{ s.Time }}</td>
                    <td>
                      <RouterLink :to="'/Book/' + s.ID"><button class="open-button">Book now</button></RouterLink>
                    </td>
                  </tr>
                </table>
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary">Save changes</button>
              </div>
            </div>
          </div>
        </div>
        <ul class="navbar-nav me-5 mb-2 mb-lg-0 ms-4">
          <!-- ..........................................if not login.................. -->

          <li v-if="!isLoggedIn" class="nav-item">
            <div class="modal fade" id="exampleModalToggle" aria-hidden="true" aria-labelledby="exampleModalToggleLabel"
              tabindex="-1">
              <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content">
                  <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalToggleLabel">
                      Get Started
                    </h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <form @submit.prevent="login" method="POST">
                      <div class="mb-3">
                        <label for="exampleInputEmail1" class="form-label">Email address</label>
                        <input v-model="email" type="email" class="form-control" name="user_id"
                          placeholder="name@example.com" required />
                        <div id="emailHelp" class="form-text">
                          We'll never share your email with anyone else.
                        </div>
                      </div>
                      <div class="mb-3">
                        <label for="exampleInputPassword1" class="form-label">Password</label>
                        <input v-model="password" type="password" class="form-control" name="password"
                          placeholder="Password" />
                      </div>
                      <button type="submit" class="btn btn-primary" data-bs-dismiss="modal">
                        Login
                      </button>
                    </form>
                  </div>
                  <div class="modal-footer">
                    <button class="btn btn-primary" data-bs-target="#exampleModalToggle2" data-bs-toggle="modal">
                      Not a member? SignIn
                    </button>
                  </div>
                </div>
              </div>
            </div>
            <div class="modal fade" id="exampleModalToggle2" aria-hidden="true" aria-labelledby="exampleModalToggleLabel2"
              tabindex="-1">
              <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content">
                  <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalToggleLabel2">
                      Create an account
                    </h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <form @submit.prevent="signup" method="POST" enctype="multipart/form-data">
                      <div class="mb-3">
                        <label for="exampleInputPassword1" class="form-label">First Name</label>
                        <input v-model="fname" name="fname" class="form-control" />
                        <!-- <div class="alert alert-danger p-1" role="alert" v-if="v$.fname.$error">First Name is required.</div> -->
                      </div>
                      <div class="mb-3">
                        <label for="exampleInputPassword1" class="form-label">Last Name</label>
                        <input v-model="lname" name="lname" class="form-control" />
                      </div>
                      <div class="mb-3">
                        <label for="exampleInputEmail1" class="form-label">Designation</label>
                        <div class="form-check">
                          <input class="form-check-input" v-model="designation" type="radio" name="designation" id="Admin"
                            value="admin">
                          <label class="form-check-label" for="Admin">
                            Admin
                          </label>
                        </div>
                        <div class="form-check">
                          <input class="form-check-input" v-model="designation" type="radio" name="designation"
                            id="Member" value="Member" checked>
                          <label class="form-check-label" for="Member">
                            Member
                          </label>
                        </div>
                      </div>
                      <div class="mb-3">
                        <label for="exampleInputPassword1" class="form-label">Phone Number</label>
                        <input v-model="ph_num" name="ph_num" class="form-control" />
                      </div>
                      <div class="mb-3">
                        <label for="exampleInputPassword1" class="form-label">Address</label>
                        <input v-model="address" name="address" class="form-control" />
                      </div>
                      <div class="mb-3">
                        <label for="exampleInputEmail1" class="form-label">Email address</label>
                        <input v-model="email" name="email" type="email" class="form-control" id="exampleInputEmail1"
                          aria-describedby="emailHelp" />
                        <!-- <div class="alert alert-danger p-1" role="alert" v-if="v$.user_id.$error">Please enter a valid email</div> -->
                      </div>
                      <div class="mb-3">
                        <label for="exampleInputPassword1" class="form-label">Password</label>
                        <input v-model="password" name="password" class="form-control" type="password" />
                        <!-- <div id="passwordHelp" class="alert alert-danger p-1" role="alert" v-if="v$.password.$error">Please enter a valid password</div> -->
                      </div>
                      <div class="mb-3">
                        <label for="exampleInputPassword1" class="form-label">ReEnter Password</label>
                        <input v-model="repassword" name="password" class="form-control" type="password" />
                        <!-- <div id="passwordHelp" class="alert alert-danger p-1" role="alert" v-if="v$.re-password.$error">Password doesn't match</div> -->
                      </div>

                      <button type="submit" class="btn btn-primary" data-bs-dismiss="modal">
                        Sign Up
                      </button>
                    </form>
                  </div>
                  <div class="modal-footer">
                    <button class="btn btn-primary" data-bs-target="#exampleModalToggle" data-bs-toggle="modal"
                      data-bs-dismiss="modal" aria-label="Close">
                      Back to LogIn
                    </button>
                  </div>
                </div>
              </div>
            </div>
            <button class="btn btn-primary" data-bs-target="#exampleModalToggle" data-bs-toggle="modal"
              data-bs-dismiss="modal" aria-label="Close">
              LogIn
            </button>
          </li>
          <!-- ....................................else............................................. -->
          <!-- <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="/UserView.vue">Hii! UserName</a>
        </li> -->
          <!-- <li v-else class="nav-item">
            <a class="nav-link active" aria-current="page" href="/UserView.vue">Hii! {{ fname + lname }}</a>
          </li> -->
          <li v-else class="nav-item">
            <a class="nav-link active" aria-current="page" href="/UserView.vue">Hii! {{ name }}</a>
            <button class="btn btn-primary" @click="logout()">
              LogOut
            </button>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import router from "@/router";
export default {
  name: "NavBar",
  name: "CreateForm",
  data: function () {
    return {
      isLoggedIn: localStorage.getItem('access_token') !== null,
      name: localStorage.getItem('username') ,
      fname: "",
      lname: "",
      email: "",
      password: "",
      repassword: "",
      ph_num: "",
      address: "",
      designation: "",
      searchstring: "",
      shows:[]
    };
  },

  methods: {
    search() {
      fetch("http://127.0.0.1:8000/api/search", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
        },
        body: JSON.stringify({ searchstring: this.searchstring }),
      })
        .then(res => res.json())
        .then(data => {
          console.log(data);
          this.shows = data;
        })
    },
    login() {
      if (this.email && this.password) {
        const obj = {
          email: this.email,
          password: this.password
        }
        console.log(obj);
        fetch("http://127.0.0.1:8000/api/login", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
          },
          body: JSON.stringify(obj),
        })
          .then((response) => {
            if (!response.ok) {
              alert("Invalid response");
            }
            return response.json();
          })
          .then((data) => {
            console.log(data);
            if (data.status) {
              this.isLoggedIn = 'true'
              this.name = data.username
              localStorage.setItem("access_token", data.access_token);
              localStorage.setItem("email_id", this.email);
              localStorage.setItem("username",data.username);
              if (data.designation == 'admin'){
                this.$router.push('/admin')
              }
              else{
                this.$router.push("/user");
              }
              } else {
              this.username = null;
              this.password = null;
            }
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
    logout(){
            this.isLoggedIn = false
            localStorage.removeItem('email_id')
            localStorage.removeItem('access_token')
            localStorage.removeItem('username')
            router.push('/')
        
    },
    signup() {
      const obj = {
        email: this.email,
        password: this.password,
        name: this.fname + " " + this.lname,
        ph_num: this.ph_num,
        address: this.address,
        designation: this.designation
      };
      console.log(obj)
      // console.log(this.email);
      // var data = {"email":this.email,'password':this.password,'name':this.fname+' '+this.lname,'ph_num':this.ph_num,'address':this.address};
      // console.log(data);
      fetch("http://127.0.0.1:8000/api/member", {
        headers: {
          "Content-Type": "application/json",
        },
        method: "POST",
        body: JSON.stringify(obj),
      })
        .then((response) => {
          console.log("hello", response);
          return response.json();
        })
        .then((data) => {
          console.log(data);
          if (data.status) {
            localStorage.setItem("access_token", data.access_token);
            localStorage.setItem("email_id", this.email);
            localStorage.setItem("username",data.username);

            // router.push('/home');
          } else {
            this.errStatus = true;
            this.errormsg = data.message;
            this.fname = "";
            this.lname = "";
            this.ph_num = "";
            this.address = "";
            this.email = "";
            this.designation = "";
            this.password = null;
            this.repassword = null;
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
  }

};
</script>

<style>
.navbar {
  background-color: black;
}

.d-flex {
  width: 600px;
  margin-right: 200px;
}
</style>

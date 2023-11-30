<template>
    <div v-if="create === 'False'">
      <h1><center>{{ venue }}</center></h1>
      <table id="Show">
        <tr>
          <th>ID &nbsp; &nbsp;</th>
          <th>Name &nbsp; &nbsp;</th>
          <th>Rating &nbsp; &nbsp;</th>
          <th>Tags &nbsp; &nbsp;</th>
          <th>Ticket_Price &nbsp; &nbsp;</th>
          <th>Edit Show &nbsp; &nbsp;</th>
          <th>Delete Show &nbsp; &nbsp;</th>
          <th>Book Show</th>
        </tr>
  
        <tr v-for="s in shows" :key="s.ID">
          <td>{{ s.ID }}</td>
          <td>{{ s.Name }}</td>
          <td>{{ s.Rating }}</td>
          <td>{{ s.Tags }}</td>
          <td>{{ s.Ticket_Price }}</td>
          <!-- <td v-if="isAdmin"> -->
            <!-- <a :href="getEditShowUrl(s.ID, VID)"><button>Edit</button></a>
          </td>
          <td v-if="isAdmin">
            <a :href="getDeleteShowUrl(s.ID, VID)"><button>Delete</button></a>
          </td>
          <td> -->
            <!-- <button @click="bookShow(s.ID, VID)" class="open-button">Book now</button>
          </td> -->
        </tr>
      </table>
    </div>
  
    <div v-else>
      <div
        style="
          margin-top: 70px;
          margin-left: 550px;
          margin-right: 550px;
          padding: 2em;
          padding-top: 0em;
          position: absolute;
          border-radius: 10px;
          border: 5px solid rgb(75, 24, 177);
          background-color: rgba(39, 40, 33, 0.7);
        "
      >
        <form @submit.prevent="createShow" method="POST" id="create-form">
          <h3
            style="
              margin-left: 20px;
              margin-bottom: 20px;
              margin-top: 20px;
              color: rgb(219, 97, 211);
              font-weight: bold;
              font-family: Georgia, 'Times New Roman', Times, serif;
              text-shadow: 2px 1px white;
            "
          >
            Create Shows
          </h3>
          <div style="color: aquamarine;" class="mb-3">
            <label for="exampleInputEmail1" class="form-label">Name</label>
            <input
              type="text"
              v-model="newShow.Name"
              class="form-control"
              id="exampleInputEmail1"
              aria-describedby="emailHelp"
              required
            />
          </div>
          <div style="color: aquamarine;" class="mb-3">
            <label for="exampleInputEmail1" class="form-label">Rating</label>
            <input
              type="text"
              v-model="newShow.Rating"
              class="form-control"
              id="exampleInputEmail1"
              aria-describedby="emailHelp"
              required
            />
          </div>
          <div style="color: aquamarine;" class="mb-3">
            <label for="exampleInputEmail1" class="form-label">Tags</label>
            <input
              type="text"
              v-model="newShow.Tags"
              class="form-control"
              id="exampleInputEmail1"
              aria-describedby="emailHelp"
              required
            />
          </div>
          <div style="color: aquamarine;" class="mb-3">
            <label for="exampleInputEmail1" class="form-label">Time</label>
            <input
              type="datetime-local"
              v-model="newShow.Time"
              class="form-control"
              id="exampleInputEmail1"
              aria-describedby="emailHelp"
              required
            />
          </div>
          <div style="color: aquamarine;" class="mb-3">
            <label for="exampleInputEmail1" class="form-label">Ticket_Price</label>
            <input
              type="text"
              v-model="newShow.Ticket_Price"
              class="form-control"
              id="exampleInputEmail1"
              aria-describedby="emailHelp"
              required
            />
            <br />
            <button type="submit" value="submit" class="btn btn-primary">Save Changes</button>
            <br />
          </div>
        </form>
      </div>
    </div>
  
    <!-- <button v-if="isAdmin" @click="goToAddShowPage">Create</button> -->
  </template>
  
  <script>
  export default {
    name: "shows",
    props: ['create', 'venue', 'shows', 'isAdmin', 'VID'], // Assuming these props are passed from the parent component
    data() {
      return {
        newShow: {
          venueid:this.$route.params['venue_id'],
          Name: '',
          Rating: '',
          Tags: '',
          Time: '',
          Ticket_Price: '',
        },
      };
    },
    methods: {
      createShow() {
        fetch("http://127.0.0.1:8000/api/shows", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
        },
        body: JSON.stringify(this.newShow),
      })
      .then(res => res.json())
      .then(data => {
        if(data.error){
          alert (data.error)
        }
        else{  console.log(data);
          alert('show created successfully')}
          this.newShow.Name=  '',
          this.newShow.Rating= '',
          this.newShow.Tags= '',
          this.newShow.Time= '',
          this.newShow.Ticket_Price= ''
        });
        // console.log('Create Show -', this.newShow);
      },
      goToAddShowPage() {
        // Implement navigation to the add show page, if applicable
        // For example, you can use Vue Router to navigate to the page
      },
    },
  };
  </script>
  
<template>
    <div>
      <a :href="'http://127.0.0.1:8000/venue_report/' + venueid">
    <button class="btn btn-primary">View Report</button>
  </a>
      <h1><center>shows </center></h1>
      <table id="Show">
        <tr>
          <th>ID &nbsp; &nbsp;</th>
          <th>Name &nbsp; &nbsp;</th>
          <th>Rating &nbsp; &nbsp;</th>
          <th>Tags &nbsp; &nbsp;</th>
          <th>Ticket_Price &nbsp; &nbsp;</th>
          <th>Time &nbsp; &nbsp;</th>      
          <th>Edit Show &nbsp; &nbsp;</th>
          <th>Delete Show &nbsp; &nbsp;</th>
        </tr>
        <tr v-for="s in shows" :key="s.ID">
          <td>{{ s.ID }}</td>
          <td>{{ s.Name }}</td>
          <td>{{ s.Rating }}</td>
          <td>{{ s.Tags }}</td>
          <td>{{ s.Ticket_Price }}</td>
          <td>{{ s.Time }}</td>
          <td>
          <a><button class="btn btn-primary" data-bs-toggle="modal" :data-bs-target="'#edit' + s.ID">Edit</button></a>
          </td>
            <!-- Modal -->
            <div class="modal fade" :id="'edit' + s.ID" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
              <div class="modal-dialog">
              <div class="modal-content">
                <div class="modal-header">
                  <h5 class="modal-title" id="exampleModalLabel">Edit Venue</h5>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <form @submit.prevent="updateshow(s.ID)" method="POST">
                  <div class="modal-body">
                  <div>
                    <label for="venueName">Shown Name:</label>
                    <input type="text" id="showName" v-model="showData.Name" required />
                  </div>
                  <div>
                    <label for="venuePlace">Ticket Price:</label>
                    <input type="text" id="showPlace" v-model="showData.Price" />
                  </div>
                  <div>
                    <label for="venueCapacity">Show Time:</label>
                    <input type="datetime-local" id="showtime" v-model="showData.Time" />
                  </div>
                  </div>
                  <div class="modal-footer">
                    <button type="submit" class="btn btn-primary" data-bs-dismiss="modal">Save changes</button>
                  </div>
                </form>

              </div>
            </div>
        </div>
          <td>
            <a><button class="btn btn-primary" @click="deleteshow(s.ID)" onclick="return confirm('Are you sure you want to delete your venue?');">Delete</button></a>
           </td> 
          
        </tr>
      </table>
    </div>
</template>
  
  <script>
import { RouterLink } from 'vue-router';

  export default {
    data() {
      return {
          venueid:this.$route.params['venue_id'],
          shows:[],
          showData: {
            Name:'',
            Price:'',
            Time:''
            }
          };
    },
    mounted() {
        fetch("http://127.0.0.1:8000/api/shows/"+this.venueid, {
            method: "GET",
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
           Authorization: "Bearer " + localStorage.getItem("access_token")

        },
      })
      .then(res => res.json())
      .then(data => {
          console.log(data);
          this.shows = data;
        });
    },

    methods:{

 updateshow(show_id) {
  this.showData['show_id']=show_id
fetch(`http://127.0.0.1:8000/api/shows`, {
  method: "PUT",
  headers: {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
    Authorization: "Bearer " + localStorage.getItem("access_token")
  },
  body: JSON.stringify(this.showData)
})
  .then(res => res.json())
  .then(data => {
    if(data.error){
      alert (data.error)
    }
    console.log(data);
  })
  .catch(error => {
    console.error("Error:", error);
    
  });
},

deleteshow(show_id){
  fetch("http://127.0.0.1:8000/api/shows/"+show_id, {
method: "DELETE",
headers: {
  "Content-Type": "application/json",
  "Access-Control-Allow-Origin": "*",
  Authorization: "Bearer " + localStorage.getItem("access_token")
}
})
.then(res => res.json())
.then(data => {
  if(data.error){
      alert (data.error)
    }
  console.log(data);
  
})
.catch(error => {
  console.error("Error:", error);
  
});


},
    },
    components: { RouterLink }
}
  
 
</script> 
  
  
  
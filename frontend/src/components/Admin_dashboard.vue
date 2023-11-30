<template>
    <div>
      <h1><center>Venue</center></h1>
      <table style="border: 5px solid green;" id="Venue">
        <tr>
          <th>&nbsp;&nbsp;ID&nbsp;&nbsp;</th>
          <th>Name&nbsp;&nbsp;</th>
          <th>Place&nbsp;&nbsp;</th>
          <th>Capacity&nbsp;&nbsp;</th>
          <th>Edit Venue&nbsp;&nbsp;</th>
          <th>Delete Venue&nbsp;&nbsp;</th>
        </tr>
        <tr v-for="venue in venues" :key="venue.ID">
          <td><RouterLink :to="'/venue_show/'+venue.ID">&nbsp;&nbsp;{{ venue.ID }}</RouterLink></td>
          <td><RouterLink :to="'/shows/'+venue.ID">{{ venue.Name }}</RouterLink></td>
          <td>{{ venue.Place }}</td>
          <td>&nbsp; &nbsp;{{ venue.Capacity }}</td>
          <td>
            <a>
              <button type="button" class="btn btn-primary" data-bs-toggle="modal" :data-bs-target="'#edit' + venue.ID">Edit</button>
            </a>
          </td>
          <td>
             <a @click="deletevenue(venue.ID)"  onclick="return confirm('Are you sure you want to delete your venue?');"> 
               <button type="button" class="btn btn-primary" >
                Delete
              </button>
            </a> 
          </td>
                <!-- Modal -->
                <div class="modal fade" :id="'edit' + venue.ID" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
              <div class="modal-dialog">
              <div class="modal-content">
                <div class="modal-header">
                  <h5 class="modal-title" id="exampleModalLabel">Edit Venue</h5>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <form @submit.prevent="updateVenue(venue.ID)" method="POST">
                  <div class="modal-body">
                  <div>
                    <label for="venueName">Venue Name:</label>
                    <input type="text" id="venueName" v-model="venueData.Name" required />

                  </div>
                  <div>
                    <label for="venuePlace">Venue Place:</label>
                    <input type="text" id="venuePlace" v-model="venueData.Place" />
                  </div>
                  <div>
                    <label for="venueCapacity">Venue Capacity:</label>
                    <input type="number" id="venueCapacity" v-model="venueData.Capacity" />
                  </div>
                  </div>
                  <div class="modal-footer">
                    <button type="submit" class="btn btn-primary" data-bs-dismiss="modal">Save changes</button>
                  </div>
                </form>

              </div>
            </div>
        </div>
        </tr>
      </table>
      <br>
  </div>
  
</template>
  
  <script>
import { RouterLink } from 'vue-router';

  export default {
    data() {
        return {
            create: 'False',
            venues: [],
            venueData: {
                Place: '',
                Capacity: '',
                Name: ''
            },
        };
    },
    mounted() {
        fetch("http://127.0.0.1:8000/api/add_venue", {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                Authorization: "Bearer " + localStorage.getItem("access_token")
            }
        })
            .then(res => res.json())
            .then(data => {
            console.log(data);
            this.venues = data;
        });
    },

    methods:{

      updateVenue(venue_id) {
        this.venueData['venue_id'] = venue_id;
      fetch(`http://127.0.0.1:8000/api/add_venue`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
          Authorization: "Bearer " + localStorage.getItem("access_token")
        },
        body: JSON.stringify(this.venueData)
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

    deletevenue(venue_id){
        fetch("http://127.0.0.1:8000/api/add_venue/"+venue_id, {
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



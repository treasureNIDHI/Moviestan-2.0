<template>
    <div>
      <h1><center>shows </center></h1>
      <table id="Show">
        <tr>
          <th>ID &nbsp; &nbsp;</th>
          <th>Name &nbsp; &nbsp;</th>
          <th>Rating &nbsp; &nbsp;</th>
          <th>Tags &nbsp; &nbsp;</th>
          <th>Ticket_Price &nbsp; &nbsp;</th>
          <th>Time &nbsp; &nbsp;</th>
          

          <!-- <th>Edit Show &nbsp; &nbsp;</th>
          <th>Delete Show &nbsp; &nbsp;</th> -->
          <th>Book Show</th>
        </tr>
  
        <tr v-for="s in shows" :key="s.ID">
          <td>{{ s.ID }}</td>
          <td>{{ s.Name }}</td>
          <td>{{ s.Rating }}</td>
          <td>{{ s.Tags }}</td>
          <td>{{ s.Ticket_Price }}</td>
          <td>{{ s.Time }}</td>

          <!-- <td v-if="isAdmin"> -->
            <!-- <a :href="getEditShowUrl(s.ID, VID)"><button>Edit</button></a>
          </td>
          <td v-if="isAdmin">
            <a :href="getDeleteShowUrl(s.ID, VID)"><button>Delete</button></a>
           </td> -->
          <td> 
            
            <RouterLink :to="'/Book/'+s.ID"><button  class="open-button">Book now</button></RouterLink>
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
          shows:[]
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
    
    components: { RouterLink }
}
  
 
</script> 
  
  
  
<template>
    <div>
      <h1><center>Existing Venues</center></h1>
      <table style="border: 5px solid green;" id="Venue">
        <tr>
          <th>&nbsp;&nbsp;ID&nbsp;&nbsp;</th>
          <th>Name&nbsp;&nbsp;</th>
          <th>Place&nbsp;&nbsp;</th>
          <th>Capacity&nbsp;&nbsp;</th>
          
          
        </tr>
        <tr v-for="venue in venues" :key="venue.ID">
          <td>&nbsp;&nbsp;{{ venue.ID }}</td>
          <RouterLink :to="'/show_list/'+venue.ID"><td>{{ venue.Name }}</td></RouterLink>
          <td>{{ venue.Place }}</td>
          <td>&nbsp; &nbsp;{{ venue.Capacity }}</td>
          
          <td>
            
          </td>
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
                Name: '',
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
    
    components: { RouterLink }
}
  
 
</script> 
  
  
  
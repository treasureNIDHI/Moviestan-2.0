<!-- <template>
    <div>
      <h1><center>All Bookings</center></h1>
      <table id="Book">
        <tr>
          <th>ID &nbsp; &nbsp;</th>
          <th>Show ID &nbsp; &nbsp;</th>
          <th>Price &nbsp; &nbsp;</th>
          <th>Number of Tickets &nbsp; &nbsp;</th>
          <th>Show Time &nbsp; &nbsp;</th>
          <th>Cancel</th>
        </tr>
  
        <tr v-for="b in Booked_tickets" :key="s.ID">
          <td>{{ b.ID }}</td>
          <td>{{ b.show_id }}</td>
          <td>{{ s.Price }}</td>
          <td>{{ s.Number_of_tickets }}</td>
          <td>{{ s.Timing }}</td>
           <td v-if="isAdmin"> -->
            <!-- <a :href="getEditShowUrl(s.ID, VID)"><button>Edit</button></a>
          </td>
          <td v-if="isAdmin">
            <a :href="getDeleteShowUrl(s.ID, VID)"><button>Delete</button></a>
           </td> -->
          <!-- <td> 
            
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
<template>
    <h1>this is bookings</h1>
</template> -->
 
<template>
  <div>
    
      <h2>Bookings for user {{ user }}:</h2>
      <ul>
        <li v-for="booking in bookings" :key="booking.Booking_ID">
          Booking ID: {{ booking.Booking_ID }}, Show ID: {{ booking.Show_ID }},
          Price: ${{ booking.Price }}, Tickets: {{ booking.Number_of_Tickets }},
          <button @click="cancelShow(booking.Booking_ID)">Delete</button>

        </li>
        
      </ul>
      <hr />
    
  </div>
</template>

<script>
export default {
  data() {
    return {
      bookings: [],
      user : localStorage.getItem('email_id')
    };
  },
  created() {
    this.organizeBookingsByUser();
  },
 
  methods: {
    cancelShow(b_id){
    fetch('http://127.0.0.1:8000/api/book_show/'+b_id, {
          method: 'DELETE',
          headers: {
            'Content-Type': 'application/json',
            "Access-Control-Allow-Origin": "*",
            Authorization: "Bearer " + localStorage.getItem("access_token")
          }
        })

  },
    organizeBookingsByUser() {
      for (const booking of this.bookings) {
        if (!this.bookingsByUser[booking.User_email]) {
          this.$set(this.bookingsByUser, booking.User_email, []);
        }
        this.bookingsByUser[booking.User_email].push(booking);
      }
    },
  },
  mounted() {
        fetch("http://127.0.0.1:8000/api/book_show", {
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
            this.bookings = data;
        });
    },

};
</script>

<style>

</style>

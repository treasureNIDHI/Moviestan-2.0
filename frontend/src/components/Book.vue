<template>
  <div>
    <h2>{{ shows.Name }}</h2>
    <p>Venue: {{ shows.venue_name }}</p>    
    <p>Ticket Price: {{ shows.Ticket_Price }}</p>
    <p>Show Time: {{ shows.Time }}</p>
    <p>Available Tickets: {{ shows.capacity - shows.Booked_tickets }}</p>

    <form @submit.prevent="bookShow" class="form-container" method="POST">
      <label for="Number_of_Tickets">Number of Tickets:</label>
      <input
        type="number"
        placeholder="Number of tickets"
        v-model="numberOfTickets"
        required
      />
      <button type="submit" id="booked">Book Now</button>
    </form>
  </div>
</template>

<script>
export default {
  props:['show'],
  data() {
    return {
      show_id:this.$route.params['show_id'] , // Initialize with the show data received from the server
      numberOfTickets: 0,
      shows:[]
    };
  },
  methods: {
    bookShow() {
      console.log(this.shows.Booked_tickets,Number(this.numberOfTickets),this.shows.capacity);
      if (this.shows.Booked_tickets + Number(this.numberOfTickets) <= this.shows.capacity) {
          const bookingData = {
          Show_ID: this.shows.ID,
          Price: this.shows.Ticket_Price,
          Number_of_Tickets: Number(this.numberOfTickets)
        };
        console.log(bookingData);
        

        fetch('http://127.0.0.1:8000/api/book_show', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            "Access-Control-Allow-Origin": "*",
            Authorization: "Bearer " + localStorage.getItem("access_token")
          },
          body: JSON.stringify(bookingData)
        })
          .then(response => response.json())
          .then(data => {
            console.log(data);           
          })
          .catch(error => {
            console.log(error);
          });


        
        this.shows.Booked_tickets += this.numberOfTickets;
        this.numberOfTickets = 1; 
        alert('Booking successful!'); 
      } else {
        alert('Not enough available tickets.');
      }
    },
  },

  mounted() {
        fetch("http://127.0.0.1:8000/api/shows/0/"+this.show_id, {
            method: "GET",
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
          Authorization: "Bearer " + localStorage.getItem("access_token")

        },
      })
      .then(res => res.json())
      .then(data => {
          this.shows = data;
          console.log(data);

        });
    }


};
</script>

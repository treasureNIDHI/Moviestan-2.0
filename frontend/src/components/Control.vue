<template>
  <div>
    <h2>Add Venue Details:</h2>
    <form @submit.prevent="createVenue" method="POST">
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
      <button type="submit">Submit</button>
    </form>
    
  </div>
</template>

<script>


export default {
  data() {
    return {
      venueData: {
        Admin: localStorage.getItem("email"),
        Name: "",
        Place: "",
        Capacity: null,
      },
      showData: false,
      venues: [], // Array to store the existing Venue data fetched from the API
    };
  },

  methods: {
    createVenue() {
      this.venues.push({
        Place: this.venueData.Place,
        Capacity: this.venueData.Capacity,
        Name: this.venueData.Name,
      });

      // this.venueData.Place = "";
      // this.venueData.Capacity = "";
      // this.venueData.Name = "";

      fetch("http://127.0.0.1:8000/api/add_venue", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
          Authorization: "Bearer " + localStorage.getItem("access_token")
        },
        body: JSON.stringify(this.venueData),
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.success) {
            console.log(data);
            if(data.error){
              alert (data.error)
            }
            const newVenueId = data.id;
            this.venues.push({
              id: newVenueId,
              Place: this.venueData.Place,
              Capacity: this.venueData.Capacity,
              Name: this.venueData.Name,
            });

            this.venueData.Place = "";
            this.venueData.Capacity = "";
            this.venueData.Name = "";

            alert("Venue added successfully!");
          } else {
            console.log("Venue addition failed. Server response:", data);
            alert("Venue addition failed. Please try again later.");
          }
        })
        .catch((error) => {
          console.error(error);
          alert(
            "An error occurred while creating the venue. Please try again later."
          );
        });

      // submitVenue() {
      //   fetch("http://127.0.0.1:8000/api/venue", {
      //     headers: {
      //       "Content-Type": "application/json",
      //     },
      //     method: "POST",
      //     body: JSON.stringify(this.venueData), // Use this.venueData to get the form input values
      //   })
      //     .then((response) => {
      //       if (!response.ok) {
      //         throw new Error("Network response was not ok");
      //       }
      //       return response.json();
      //     })
      //     .then((data) => {
      //       console.log(data); // Handle the response from the API
      //       // Handle success or failure here, show messages, etc.
      //     })
      //     .catch((err) => {
      //       console.error("Error:", err);
      //       // Handle errors here, show error messages, etc.
      //     });
      // },

      // fetchExistingVenues() {
      //   fetch("http://127.0.0.1:8000/api/venue")
      //   .then((response) => {
      //     if (!response.ok) {
      //       throw new Error("Network response was not ok");
      //     }
      //     return response.json();
      //   })
      //   .then((data) => {
      //     this.existingVenues = data; // Assuming the API response is an array of existing venues
      //   })
      //   .catch((err) => {
      //     console.error("Error:", err);

      //   });
    },
  },
};
</script>

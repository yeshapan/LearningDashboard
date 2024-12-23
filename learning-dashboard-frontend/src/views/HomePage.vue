<template>
  <div class="home">
    <Navbar />
    <h1>Welcome to the Learning Dashboard!</h1>
    <p>Explore courses, track your progress, and engage with the community.</p>
  </div>
</template>

<script>
// Import Navbar to reuse the navigation component
import Navbar from '@/components/Navbar.vue';

export default {
  name: 'HomePage',
  components: {
    Navbar, // Register Navbar component
  },
};
</script>

<style>
/* Basic styling for the home page */
.home {
  text-align: center;
  padding: 20px;
}
</style>

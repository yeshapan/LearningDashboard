<template>
  <div class="dashboard">
    <Navbar />
    <h2>Your Dashboard</h2>
    <p>Here are your enrolled courses and progress.</p>
    <ul>
      <li v-for="course in courses" :key="course.id">
        {{ course.title }} - {{ course.progress }}%
      </li>
    </ul>
  </div>
</template>

<script>
// Mock data to display user's courses
export default {
  name: 'DashboardPage',
  data() {
    return {
      courses: [
        { id: 1, title: 'Intro to Vue.js', progress: 75 },
        { id: 2, title: 'Django for Beginners', progress: 50 },
      ],
    };
  },
};
</script>

<style>
/* Styling for the dashboard page */
.dashboard {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}
</style>

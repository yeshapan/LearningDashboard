<template>
  <!-- The navbar with navigation links -->
  <nav class="navbar">
    <ul>
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/login">Login</router-link></li>
      <li><router-link to="/dashboard">Dashboard</router-link></li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'Navbar',
};
</script>

<style>
/* Basic styling for the navbar */
.navbar {
  background-color: #9F2B68;
  color: whitesmoke;
  padding: 10px;
}
.navbar ul {
  list-style: none;
  display: flex;
  gap: 20px;
}
.navbar a {
  color: whitesmoke;
  text-decoration: none;
}
</style>

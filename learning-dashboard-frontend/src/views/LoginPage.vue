<template>
  <div class="login-page">
    <Navbar />
    <h2>Login</h2>
    <LoginForm />
  </div>
</template>

<script>
// Import Navbar and LoginForm components
import Navbar from '@/components/Navbar.vue';
import LoginForm from '@/components/LoginForm.vue';

export default {
  name: 'LoginPage',
  components: {
    Navbar,
    LoginForm,
  },
};
</script>

<style>
/* Styling for the login page */
.login-page {
  max-width: 600px;
  margin: 0 auto;
  text-align: center;
  padding: 20px;
}
</style>

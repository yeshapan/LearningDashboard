<template>
  <form @submit.prevent="handleLogin">
    <!-- Email input -->
    <label>Email:
      <input type="email" v-model="email" />
    </label>
    <!-- Password input -->
    <label>Password:
      <input type="password" v-model="password" />
    </label>
    <!-- Submit button -->
    <button type="submit">Login</button>
  </form>
</template>

<script>
export default {
  name: 'LoginForm',
  data() {
    return {
      email: '', // User's email
      password: '', // User's password
    };
  },
  methods: {
    // Handle login action
    async handleLogin() {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/login/', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ email: this.email, password: this.password }),
        });
        if (response.ok) {
          alert('Login successful!');
        } else {
          alert('Login failed. Please check your credentials.');
        }
      } catch (error) {
        console.error('Error during login:', error);
        alert('An error occurred. Please try again later.');
      }
    },
  },
};
</script>

<style>
/* Styling for the login form */
form {
  display: flex;
  flex-direction: column;
  gap: 10px;
  max-width: 400px;
  margin: 0 auto;
}
label {
  font-weight: bold;
}
button {
  padding: 10px;
  background-color: #DE3163;
  color: white;
  border: none;
  cursor: pointer;
}
button:hover {
  background-color: #9F2B68;
}
</style>

<script>
import { loginUser } from '@/services/api';

export default {
  methods: {
    async handleLogin() {
      try {
        const response = await loginUser(this.email, this.password);
        alert(response.message);
      } catch (error) {
        alert(error.message);
      }
    },
  },
};
</script>


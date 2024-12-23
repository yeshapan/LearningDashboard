//this file defines routes for navigation
import Vue from 'vue';
import VueRouter from 'vue-router';
import HomePage from '@/views/HomePage.vue';
import LoginPage from '@/views/LoginPage.vue';
import DashboardPage from '@/views/DashboardPage.vue';

Vue.use(VueRouter);

const routes = [
  { path: '/', component: HomePage },
  { path: '/login', component: LoginPage },
  { path: '/dashboard', component: DashboardPage },
];

const router = new VueRouter({
  mode: 'history',
  routes,
});

export default router;

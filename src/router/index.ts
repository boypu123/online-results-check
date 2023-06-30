import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ResultsCheck from '../views/ResultsCheck.vue'
import AdminView from '../views/AdminView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/results',
      name: 'Results Check',
      component: ResultsCheck
    },
    {
      path: '/admin',
      name: 'Admin',
      component: AdminView
    },
  ]
})

export default router

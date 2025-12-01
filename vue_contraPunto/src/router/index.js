import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue';
import Comparativas from '../views/Comparativas.vue';
import Comparativa1 from '../views/Comparativa1.vue';
import Comparativa2 from '../views/Comparativa2.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/comparativas',
      name: 'Comparativas',
      component: Comparativas
    },
    {
      path: '/comparativa1',
      name: 'Comparativa1',
      component: Comparativa1
    },
    {
      path: '/comparativa2',
      name: 'Comparativa2',
      component: Comparativa2
    },
  ],
})

export default router

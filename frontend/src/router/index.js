import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import UserView from '@/views/UserView.vue'
import AdminView from '@/views/AdminView.vue'
import Bookings from '@/components/Bookings.vue'
import Control from '@/components/Control.vue'
import Profile from '@/components/Profile.vue'
import User_dashboard from '@/components/User_dashboard.vue'
import Admin_dashboard from '@/components/Admin_dashboard.vue'
import shows from '@/components/shows.vue'
import show_list from '@/components/show_list.vue'
import Book from '@/components/Book.vue'
import shows_list from '@/components/shows_list.vue'




Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path:'/user',
    name:'user',
    component: UserView,
    children:[{
      path: 'bookings',
      name: 'bookings',
      component: Bookings,
    },
    {
      path: '/user',
      name: 'user_dashboard',
      component: User_dashboard ,
    },
    {
      path: 'profile',
      name: 'profile',
      component: Profile,
    },
    {
    path:'/show_list/:venue_id',
    name:'show_list',
    component:show_list,
    },
    {
    path:'/Book/:show_id',
    name:'Book',
    component:Book,
    }
  ]
  },
  {
    path:'/admin',
    name:'admin',
    component: AdminView,
    children:[{
      path: '/admin',
      name: 'dashboard',
      component: Admin_dashboard,
    },
      
    {
      path: 'control',
      name: 'control',
      component: Control,
    },
    {
      path:'/shows/:venue_id',
      name:'shows',
      component:shows
    },
    {
      path:'/venue_show/:venue_id',
      name:'showslist',
      component:shows_list
    },
    {
      path: 'profile',
      name: 'profile',
      component: Profile,
    },
    
    
  ]
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Login from '@/components/Login'
import Cabinet from '@/components/Cabinet'
import Registration from '@/components/Registration'
import MyPage from '@/components/MyPage'
import Statistics from '@/components/Statistics'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/cabinet',
      name: 'cabinet',
      component: Cabinet
    },
    {
      path: '/registration',
      name: 'registration',
      component: Registration
    },
    {
      path: '/mypage',
      name: 'mypage',
      component: MyPage
    },
    {
      path: '/statistics',
      name: 'statistics',
      component: Statistics
    }
  ]
})

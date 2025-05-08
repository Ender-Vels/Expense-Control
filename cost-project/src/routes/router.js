import { createRouter, createWebHistory } from "vue-router";
import Home from '../components/Home.vue'
import Login from '../components/Login.vue'
import Register from '../components/Register.vue'
import Dashboard from '../components/Dashboard/Dashboard.vue'
import Income from '../components/Dashboard/Income.vue'
import Expenses from "../components/Dashboard/Expenses.vue";


let route = createRouter({
    history: createWebHistory(),
    routes:[
        {
            path: '/',
            name: 'home',
            component: Home,
        },
        {
            path: '/login',
            name: 'login',
            component: Login,
            
        },
        {
            path: '/register',
            name: 'register',
            component: Register,
            
        },
        {
            path: '/dashboard',
            name: 'dashboard',
            component: Dashboard,
            meta:{requiresAuth:true}
            
        },
        {
            path: '/income',
            name: 'income',
            component: Income,
            meta:{requiresAuth:true}
            
        },
        {
            path: '/expenses',
            name: 'expenses',
            component: Expenses,
            meta:{requiresAuth:true}
            
        },
        
    ]
})

route.beforeEach((to,from,next)=>{
    const token = localStorage.getItem('token')

    if(to.meta.requiresAuth && !token){
        next({name:'login'})
    }
    else if((to.name === 'login'|| to.name === 'register')&& token){
        next({name:'dashboard'})
    }
    else{
        next()
    }
})

export default route
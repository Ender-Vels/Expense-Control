import { defineStore } from 'pinia'
import axios from 'axios'
import { jwtDecode } from 'jwt-decode'


export let user_store = defineStore('users',{
    state:()=>({
        token:null,
        is_auth: false,
        message: '',

    }),
    getters:{
        get_name(){
            let acc_token = localStorage.getItem('token')
            if (acc_token){
                let data =  jwtDecode(acc_token)
                console.log(data)
                return data.login
            }
            else{
                return "Nothing token"
            }
        },
        get_id(){
            let acc_token = localStorage.getItem('token')
            if (acc_token){
                let data =  jwtDecode(acc_token)
                console.log(data)
                return data.id
            }
            else{
                return "Nothing token"
            }
        },
        get_token:(state)=>{
            let acc_token = localStorage.getItem('token')
            if (acc_token){
                return acc_token
            }
            else{
                return "Nothing token"
            }
        }
    },
    actions:{
        // set auth status
        set_auth_status(){
            let acc_token = localStorage.getItem('token')
            if (acc_token){
                this.is_auth = true
            }
            else{
                this.is_auth = false
            }
        },
        //register user
        async register_user(data,router){
            try{
                let response = await axios.post("http://127.0.0.1:8000/register",data)
                alert(response.data.message)
                router.push('/login')

            }
            catch(error){
                alert(error.response.data.detail)
            }
        },
            //auth user
        async auth_user(data,router){
            try{
                let response = await axios.post('http://127.0.0.1:8000/auth', data)
                this.token = response.data.access_token
                localStorage.setItem('token',this.token)
                this.token = null
                this.set_auth_status()
                router.push({name:'dashboard'})

                
            }   
            catch(error){
                alert(error.response.data.detail)
            }
        },
        //logout user
        logout_user(router){
            localStorage.removeItem('token')
            this.token = null
            this.is_auth = false
            router.push('/login')
        },
        //refresh token
        async refresh_token(){
            let token = this.get_token
            let token_data = {
                token: token
            }
            try{
                let response = await axios.post('http://127.0.0.1:8000/refresh_token', token_data)
                localStorage.removeItem('token')
                this.token = response.data.access_token
                localStorage.setItem('token',this.token)
                this.token = null
            }
            catch(error){
                console.log(error)
            }
        },
        //change login
        async change_login(data){
            try{
                let response = await axios.put('http://127.0.0.1:8000/put_login', data)
                alert(response.data.message)
            }
            catch(error){
                console.error(error)
            }
        },
        //change email
        async change_email(data){
            try{
                let response = await axios.put('http://127.0.0.1:8000/change_email', data)
                alert(response.data.message)
            }
            catch(error){
                console.error(error)
            }
        },
        //change password
        async change_password(data){
            try{
                let response = await axios.put('http://127.0.0.1:8000/change_password', data)
                alert(response.data.message)
            }
            catch(error){
                console.error(error)
            }
        },
        
    },


})
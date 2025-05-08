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
        async register_user(login,password,confirm_password,email,phone,router){
            if(String(login).length >= 2 ){

                if(String(password).length >= 6){

                    if(password == confirm_password){
                        try{
                            let data={
                                login: login,
                                password: password,
                                email: email,
                                phone: phone
                            }
                            console.log(data)
                            let response = await axios.post("http://127.0.0.1:8000/register",data)
                            alert(response.data.message)
                            this.message = response.data.message
                            router.push('/login')
                        }
                        catch(err){
                            alert(this.message)
                        }
                    }
                    else{
                        alert('Password and confirm password incorrect')
                    }

                }
                else{
                    alert('Password length must be minimum 6 symbols')
                }
            }
            else{
                alert('Login length must be minimum 2 symbols')
            }
        },
            //auth user
        async auth_user(login,password,router){
            if(String(login).length >= 2){
                console.log(password)
                if (String(password).length >=6){
                    try{
                        let data = {
                            login: login,
                            password: password
                        }
                        

                        let response = await axios.post('http://127.0.0.1:8000/auth',data)
                        this.token = response.data.access_token
                        localStorage.setItem('token',this.token)
                        this.token = null
                        this.set_auth_status()
                        router.push('/dashboard')
                    }
                    catch(err){
                        console.log(err)
                    }
                }
                else{
                    alert("Wrong! Password are Short!")
                }
            }   
            else{
                alert("Wrong! Login are Short!")
            }
        },
        //logout user
        logout_user(router){
            localStorage.removeItem('token')
            this.token = null
            this.is_auth = false
            router.push('/login')
        },
        
    },


})
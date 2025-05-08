/*Income store*/
import { defineStore } from "pinia";
import axios from "axios";

export let income_store=defineStore('income',{
    state:()=>({
        message:'',
        income_list:[],
        sum_income:0,
    }),
    getters:{
        get_incomes(state){
            if(state.income_list.length){
                return state.income_list
            }
            else{
                return "You don't have anithing incomes"
            }
        },
        getTotalIncome(){
            return this.sum_income
        }
    },
    actions:{
        async add_income(data){
            try{
                let response = await axios.post('http://127.0.0.1:8000/add_income',data)
                this.message = response.data.message
            }
            catch(err){
                console.log(err)
                
            }
        },
        async get_income_by_id(data){
            try{
                let response = await axios.post('http://127.0.0.1:8000/get_income_by_id',data)
                this.income_list = response.data.incomes
            }
            catch(err){
                console.log(err)
            }
        },
        //delete income
        async delete_income(data){
            try{
                let response = await axios.post('http://127.0.0.1:8000/delete_income',data)
                this.message = response.data.message
            }
            catch(err){
                console.log(err)
            }
        },
        // get sum of incomes by user id
        async get_sum_income(id){
            try{
                let response = await axios.post('http://127.0.0.1:8000/get_sum_income',id)
                return  response.data.sum[0].sum
            }
            catch(err){
                console.log(err)
            }
        
        }
    }
})
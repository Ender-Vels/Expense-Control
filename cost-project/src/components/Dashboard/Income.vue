<template>
    <Header/>
    <div class="income">
        <!--Add new Income-->
        <div class="income_add">
            <div class="income_logo">
                <div class="income_logo_logo">
                    <img src="../../assets/dash/money.png" alt="">
                </div>
                <div class="income_logo_title">
                    <h2>Input Income Money to Balance</h2>
                </div>
            </div>
            <div class="income_addForm">
                <!--Form to add money-->
                <div>
                    <div class="icome_input">
                        <div class="input_btn">
                            <button @click='minus_10'>-10</button>
                            <button @click='minus_100'>-100</button>
                            <button @click='minus_1000'>-1000</button>
                        </div>
                        <input type="text" v-model="money" @keydown="blockNonDigits">
                        <div class="input_btn">
                            <button @click="plus_10">+10</button>
                            <button @click="plus_100">+100</button>
                            <button @click="plus_1000">+1000</button>
                        </div>
                    </div>                
                    <div class="categories_type">
                        <!--Type income-->
                        <div class="categories_type_card" v-for="(typer,index) in categories" :key="typer.id" :class="{ active: choosen_category === typer.id }" @click="choose_category(typer.id)">
                            <div class="categories_type_logo">
                                <img :src="typer.img" alt="categorie">
                            </div>
                            <div class="categories_type_title">
                                <p>{{ typer.name }}</p>
                            </div>
                        </div>
                    </div>
                    <div class="submit_income">
                        <button @click="income_add(money,choosen_category)">Submit</button>
                    </div>
                </div>
            </div>
               
        </div>
        <!--Income history-->
        <div class="income_history" v-if="typeof inc_store.get_incomes === 'string'">
                {{ inc_store.get_incomes }}
        </div>
        <div class="income_history"  v-else>
           <div class="income_history_item" 
            v-for="(income,index) in  inc_store.get_incomes" 
            :key="income.id"
            
            >
            <!--Name income-->
                <div class="income_history_name">
                    <p>{{ get_names_category(income.type_id) }}</p>
                </div>
                <!--Sum Income-->
                <div class="income_history_sum">
                    <p>{{ income.money }} USD</p>
                </div>
                <!--Date income-->
                <div class="income_history_date">
                    <p>{{ income.date }}</p>
                </div>
                <!--Delete Income-->
                <div class="income_history_delete">   
                    <button @click="delete_income_by_id(income.id)">X</button>

                </div>
           </div>
        </div>
    </div>
</template>

<script setup>
import { ref,onMounted } from 'vue';
import Header from './Header.vue'
import { income_store } from '../../store/income_store';
import { user_store } from '../../store/user_store';
let inc_store = income_store()
let usr_store = user_store()

let money = ref(0)
let choosen_category = ref(null)
let categories = [
    {id:1,name:'Salary',img:'/src/assets/dash/Income/salary.png'},
    {id:2,name:'Loan',img:'/src/assets/dash/Income/loan.png'},
    {id:3,name:'Credit',img:'/src/assets/dash/Income/credit.png'},
    {id:4,name:'Gift',img:'/src/assets/dash/Income/giftbox.png'},
    {id:5,name:'Winning',img:'/src/assets/dash/Income/success.png'},
    {id:6,name:'Bonus',img:'/src/assets/dash/Income/bonus.png'},
]
function plus_10(){
    money.value = Number(money.value)+10
}
function plus_100(){
    money.value = Number(money.value)+100
}
function plus_1000(){
    money.value = Number(money.value)+1000
}
function minus_10(){
    money.value = Number(money.value)-10
    if (Number(money.value)<0){
        money.value = 0
    }
}
function minus_100(){
    money.value = Number(money.value)-100
    if (Number(money.value)<0){
        money.value = 0
    }
}
function minus_1000(){
    money.value = Number(money.value)-1000
    if (Number(money.value)<0){
        money.value = 0
    }
}
//Blok str
function blockNonDigits(event) {
  const allowedKeys = ['Backspace', 'ArrowLeft', 'ArrowRight', 'Delete', 'Tab']

  if (
    !/^\d$/.test(event.key) && // если не цифра
    !allowedKeys.includes(event.key) // и не служебная клавиша
  ) {
    event.preventDefault()
  }
}
//Choose category
function choose_category(id) {
  if (choosen_category.value === id) {
    choosen_category.value = null 
  } else {
    choosen_category.value = id 
  }
}
//Add income to DB
async function income_add(moneys,type_id){
    if (parseFloat(money.value) == 0){
        alert('Please fill all fields')
    }else{
    let usr_id = usr_store.get_id
    let data={
        user_id: usr_id,
        money: parseFloat(moneys),
        date: new Date().toISOString().split('T')[0],
        type_id: type_id
    }
    console.log(data)
    await inc_store.add_income(data)
    money.value = 0
    choosen_category.value = null
    get_income_by_UserId()
    }
    
}
//Get all income by user id
async function get_income_by_UserId(){
    let data={
        user_id: usr_store.get_id
    }
    await inc_store.get_income_by_id(data)
}

//get names category by id
function get_names_category(id){
    let type_category = categories.find(elem => elem.id == id)
    return type_category.name
}

//Delete income by id
async function delete_income_by_id(ic_id){
    let data={
        id: ic_id
    }
    await inc_store.delete_income(data)
    get_income_by_UserId()
}


//Mounted
onMounted(()=>{
    get_income_by_UserId()
})
</script>

<style>

</style>
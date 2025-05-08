<template>
    <Header/>
    <div class="expense">
        
        <!--Add new Expense-->
        <div class="expense_add">
            <div class="expense_logo">
                <div class="expense_logo_logo">
                    <img src="../../assets/dash/money.png" alt="">
                </div>
                <div class="expense_logo_title">
                    <h2>Input Expense Money to Balance</h2>
                </div>
            </div>
            <div class="expense_addForm">
                <!--Form to add money-->
                <div>
                    <div class="expense_input">
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
                        <!--Type expense-->
                        <div class="categories_type_card" v-for="(typer,index) in expense_store.get_expenses_typer" :key="typer.id" :class="{ active: choosen_category === typer.id }" @click="choose_category(typer.id)">
                            <div class="categories_type_logo">
                                
                                <img :src="typer.img" alt="categorie">
                            </div>
                            <div class="categories_type_title">
                                <p>{{ typer.name }}</p>
                            </div>
                        </div>
                    </div>
                    <div class="submit_expense">
                        <button @click="expense_add(choosen_category)">Submit</button>
                    </div>
                </div>
            </div>
               
        </div>
        <!--Expense history-->
        <div class="expense_history" v-if="typeof expense_store.get_expenses === 'string'">

        </div>
        <div class="expense_history" v-else>
            <div class="expense_history_item" 
                v-for="(expense, index) in expense_store.get_expenses" 
                :key="expense.id">
                
                <!--Name expense-->
                <div class="expense_history_name">
                    <p>{{ get_names_category(expense.type_id) }}</p>
                </div>
                <!--Sum Expense-->
                <div class="expense_history_sum">
                    <p>{{ expense.money }} USD</p>
                </div>
                <!--Date Expense-->
                <div class="expense_history_date">
                    <p>{{ expense.date }}</p>
                </div>
                <!--Delete Expense-->
                <div class="expense_history_delete">   
                    <button @click="delete_expense_by_id(expense.id)">X</button>
                </div>
            </div>
        </div>


    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import Header from './Header.vue'
import { useRouter } from 'vue-router'
import { expenses_store } from '../../store/expenses_store'
import { user_store } from '../../store/user_store'

let expense_store = expenses_store()
let user = user_store()
let choosen_category = ref(null)
let router = useRouter()
let money = ref(0)

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

//add expense
async function expense_add(choosen_categorye){
    if (parseFloat(money.value) == 0 || choosen_categorye == null){
        alert('Please fill all fields')
    }else{
        let id = user.get_id
        let expense = {
            user_id: id,
            money: parseFloat(money.value),
            date: new Date().toISOString().split('T')[0],
            type_id: choosen_categorye
            
        }
        await expense_store.add_expenses(expense)
        money.value = 0
        choosen_category.value = null
        get_expenses_by_UserId()

    }
}
//get expenses list
async function get_expenses_by_UserId(){
    let data={
        user_id: user.get_id
    }
    console.log(data)
    await expense_store.get_expense_by_id(data)
}

function get_names_category(id){
    let types = expense_store.get_all_typeses
    let name = types.find(type => type.id === id)
    return name.name
}

//Delete expense by id
async function delete_expense_by_id(id){
    let data = {
        id: id
    }
    await expense_store.delete_expenses(data)
    get_expenses_by_UserId()
}


onMounted(() => {
    expense_store.get_expenses_type()
    expense_store.get_all_types()
    
    get_expenses_by_UserId()
})
</script>

<style>

</style>
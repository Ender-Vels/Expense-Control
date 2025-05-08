import { defineStore } from "pinia";
import axios from "axios";


export let expenses_store = defineStore("expenses", {
  state: () => ({
    expenses_type: [],
    expenses_list: [],
    all_types: [],
    sum_expense:0,
  }),
  getters: {
    get_expenses_typer() {
      return this.expenses_type;
    },
    get_expenses() {
      return this.expenses_list;
    },
    get_all_typeses() {
      return this.all_types;
    },  
    getTotalExpenses(state) {
      return state.sum_expense;
    },
  },
  actions: {
        //get types of expenses
        async get_expenses_type() {
            try {
                let response = await axios.get("http://127.0.0.1:8000/get_expenses_type")
                this.expenses_type = response.data.expenses_type;
            }
            catch (error) {
                console.log(error);
            }
        },
        //add expenses
        async add_expenses(data) {
            try {

                let response = await axios.post("http://127.0.0.1:8000/add_expenses", data)
                console.log(response.data.message);
            }
            catch (error) {
                console.log(error);
            }
        },
        //get_expenses by user id
        async get_expense_by_id(id) {
            try {
                let response = await axios.post("http://127.0.0.1:8000/get_expenses_by_id",id)
                this.expenses_list = response.data.expenses;
              }
            catch (error) {
                console.log(error);
            }
        },
        // get all types of expenses
        async get_all_types() {
            try {
                let response = await axios.get("http://127.0.0.1:8000/get_expenses_type_name")
                this.all_types = response.data.expenses_type;
              }
            catch (error) {
                console.log(error);
            }
      },
      //delete expenses
      async delete_expenses(id) {
          try {
              let response = await axios.post("http://127.0.0.1:8000/delete_expenses",id)
              console.log(response.data.message);
            }
          catch (error) {
              console.log(error);
          }
      },
      //get all sum of expenses by user id
      async get_sum_expenses_by_id(id) {
        try {
            let response = await axios.post("http://127.0.0.1:8000/get_sum_expenses",id)
            return  response.data.sum[0].sum
          }
        catch (error) {
            console.log(error);
        }
          
    },
  }

    
});
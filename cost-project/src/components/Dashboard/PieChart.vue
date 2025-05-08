<template>
  <div class="pie_chart">
      <div class="pie_chart_title">
          <h1>Diagram of Income And Expenses</h1>
      </div>
      <div v-if="isLoading">Loading...</div>
      <div v-else>
        <Pie id="my-chart-id" :options="chartOptions" :data="chartData" />
  </div>
  </div>
  <div class="pie_data">
      <div class = income_data>
          <h2>Income: {{ Income}}</h2>
        </div>
        <div class = expenses_data>
          <h2>Expenses: {{ Expenses}}</h2>
      </div>
    </div>
  </template>
  
  <script setup>
  import { Pie } from 'vue-chartjs'
  import { Chart as ChartJS, Title, Tooltip, Legend, ArcElement, CategoryScale, LinearScale } from 'chart.js'
  import { ref, onMounted } from 'vue'
  import { income_store } from '../../store/income_store'
  import { expenses_store } from '../../store/expenses_store'
  import { user_store } from '../../store/user_store'
  
  let inc_store = income_store()
  let expense_store = expenses_store()
  let usr_store = user_store()
  
  ChartJS.register(Title, Tooltip, Legend, ArcElement, CategoryScale, LinearScale)
  
  // Реактивные переменные
  let Income = ref(0)
  let Expenses = ref(0)
  let isLoading = ref(true)
  
  let chartData = ref({
    labels: ['Expenses', 'Income'],
    datasets: [
      {
        data: [0, 0], // Данные для графика
        backgroundColor: ['#FF6384', '#36A2EB'], // Цвета для графика
        hoverBackgroundColor: ['#FF6384', '#36A2EB'],
      }
    ]
  })
  
  let chartOptions = {
    responsive: true
  }
  
  function updateChartData(Income, Expenses) {
    chartData.value = {
      ...chartData.value,
      datasets: [
        {
          ...chartData.value.datasets[0],
          data: [Expenses, Income],
        }
      ]
    }
  }
  
  onMounted(async () => {
    try {
      let my_id = usr_store.get_id;
      let ids = { user_id: my_id };
      Income.value = Number(await inc_store.get_sum_income(ids));
      Expenses.value = Number(await expense_store.get_sum_expenses_by_id(ids));
      updateChartData(Income.value, Expenses.value);
    } finally {
      isLoading.value = false;
    }
  });
  </script>
  
  <style>
  /* Стили */
  </style>
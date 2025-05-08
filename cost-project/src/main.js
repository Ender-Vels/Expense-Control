import { createApp } from 'vue'

import App from './App.vue'
import router from './routes/router'
import './style.css'
import './styles/home.css'
import './styles/login.css'
import './styles/header.css'
import './styles/side.css'
import './styles/income.css'
import './styles/expenses.css'
import './styles/dashboard.css'
import { createPinia } from 'pinia'

const pinia = createPinia()
let app = createApp(App)
app.use(router)
app.use(pinia)
app.mount('#app')

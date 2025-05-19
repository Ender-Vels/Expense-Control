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
import './styles/adaptive_dashboard.css'
import './styles/adaptive_header.css'
import './styles/adaptive_income.css'
import './styles/adaptive_expenses.css'
import './styles/change_info.css'
import './styles/adaptive_cahnege_info.css'
import './styles/adaptive_auth.css'
import './styles/adaptive_start.css'
import './styles/about.css'
import './styles/adaptive_about.css'


import { createPinia } from 'pinia'

const pinia = createPinia()
let app = createApp(App)
app.use(router)
app.use(pinia)
app.mount('#app')

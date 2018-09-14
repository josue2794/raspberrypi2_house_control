import '@babel/polyfill'
import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import ToggleButton from 'vue-js-toggle-button'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(VueAxios, axios)
Vue.use(ToggleButton)
Vue.config.productionTip = false

new Vue({
  render: h => h(App)
}).$mount('#app')



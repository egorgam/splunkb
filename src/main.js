import Vue from 'vue'
import App from './App.vue'
import Vuex from 'vuex'
import VueRouter from 'vue-router'
import axios from 'axios'
import io from 'socket.io-client';
import 'carbon-components/css/carbon-components.css';
import CarbonComponentsVue from '@carbon/vue/src/index';
Vue.use(CarbonComponentsVue);

Vue.prototype.$http = axios
Vue.use(Vuex)
Vue.use(VueRouter)


import Dashboard from './components/Dashboard.vue'

var splunkhost = 'splunkb.intranet'
// var splunkhost = 'splunk.sandbox.link'


let router = new VueRouter({
  mode: 'history',
  routes: [
    { 
      path: '/',
      alias: '/dashboard',
      name: 'dashboard',
      component: Dashboard,
    }
  ]
})

const MenuStore = {
  state: {
    current: 'dashboard',
    items: [
      ['Дашборды','dashboard'],
      ['Настройки','settings']
    ]
  }
}

const DashboardStore = {
  state: {
    job: '',
    dashboards: '',
    panels: '',
    results: [],
    splunkhost: splunkhost,
    layout: []
  },
  mutations: {
    setDashboards (state, dashboards)  {
      state.dashboards = dashboards
    }

  },
  actions: {
     getDashboards(state) {
      axios.get('https://' + splunkhost +'/api/dashboards')
      .then((response) => {
        state.commit('setDashboards', response.data);
      })
     },
     listenJobs(state) {       
      var s = io('wss://' + splunkhost +'/jobs')
        s.on('jobs', (response) =>{
          state.commit('getJobs', response.data);
        })
    }
  }
}

const store = new Vuex.Store({
  modules: {
    dashboard: DashboardStore,
    menu: MenuStore
  }
})

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})
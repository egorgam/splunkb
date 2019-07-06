<template>
  <div id="app">
   
<cv-header aria-label="Carbon header">
  <cv-skip-to-content href="#main-content">
    Skip to content
  </cv-skip-to-content>
  <cv-header-name href="javascript:void(0)" prefix=".soc">
    [Dashboard] 
  </cv-header-name>
  <div slot="header-global">
    <cv-header-global-action
      aria-label="Notifications"
      aria-controls="notifications-panel"
      @click="actionNotifications" >
      <Notification20 />
    </cv-header-global-action>
    <cv-header-global-action aria-label="User avatar" @click="actionUserAvatar" aria-controls="">
      <UserAvatar20 />
    </cv-header-global-action>
    <cv-header-global-action
      aria-label="App switcher"
      aria-controls="switcher-panel"
      @click="actionAppSwitcher">
      <AppSwitcher20 />
    </cv-header-global-action>
  </div>
</cv-header>

        <side-nav id="side-nav" ref="sidebar">
          <cv-side-nav-items>
            <selector/>
          </cv-side-nav-items>
        </side-nav>
      <router-view/>
  </div>
</template>

<script>
import Notification20 from "@carbon/icons-vue/es/notification/20";
import UserAvatar20 from "@carbon/icons-vue/es/user--avatar/20";
import AppSwitcher20 from "@carbon/icons-vue/es/app-switcher/20";
import SideNav from "./components/SideNav.vue"

import Selector from './components/Selector.vue'
export default {
  name: 'app',
  components: {
    SideNav,
    Selector,
    Notification20,
    UserAvatar20,
    AppSwitcher20
  },
  computed:{
    Vis(){
      return this.$refs.sidebar.$data
    }
  },
  methods:{
    gg(){
      var a = this.$refs.sidebar
      console.log(a)
    },
    actionNotifications(){

    },
    actionUserAvatar(){

    },
    actionAppSwitcher(){

    }
  },
    mounted(){
      this.gg()
  }
}
</script>

<style>
/* .panel {
  border: 4px solid black;
  z-index: 5;
} */
.layout {
    margin: 60px
}
.table {
  width:auto;
}
 body{
    background-color: #dddddd;
   } 
</style>

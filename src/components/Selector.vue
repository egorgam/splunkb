<template>
    <div>
        <div v-for="dashboard in $store.state.dashboard.dashboards" :key="dashboard['name']">
            <side-menu :title="dashboard['name']">
                    <selector-block :dashboard="dashboard"/>
            </side-menu>
        </div>
    </div>
</template>


<script>
import SideMenu from './carbon-custom/side-menu.vue'
import SelectorBlock from './SelectorBlock.vue'

export default {
  name: 'selector',
    data(){
    return {
      direction: 'right',
      visible: false,

    }
  },
  components: {
      SideMenu,
      SelectorBlock
  },
  created() {
    this.$store.dispatch('getDashboards')
  }
}
</script>

<style>
.item {
    cursor: pointer;
}
</style>



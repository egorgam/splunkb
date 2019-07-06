<template>
    <div>
        <div aria-haspopup="true" class="bx--side-nav__submenu">
            <div class="bx--side-nav__submenu-title">
            <color-bar :dname="dashboard['dname']"
                v-model="color"
                />
            </div>
        </div>
            <!-- <test/> -->
         <div v-for="panel in dashboard['panels']" :key="panel.id">
            <cv-side-nav-menu-item  @click="add_box(panel, dashboard['name'])" class="item">
                [{{panel['ptype']}}] {{ panel['title'] }}
            </cv-side-nav-menu-item>
        </div>
    </div>
</template>

<script>
import ColorBar from './ColorBar.vue'

export default {
    props: ['dashboard'],
    data(){
    return {
        color: {'hex':"#f3f3f3"},
        active: false
    }
  },
  components: {
      ColorBar
  },
   methods: {
    maxindex(){
        if (this.$store.state.dashboard.layout.length == 0){
            return 0
        }
        else{
            return this.$store.state.dashboard.layout.reduce((max, b) => Math.max(max, b.id), this.$store.state.dashboard.layout[0].id) + 1
        }
    },
    add_box(panel, dashboard_name){
      if (this.$store.state.dashboard.layout.filter(p => p.id == panel.id).length == 0){
        this.$store.state.dashboard.layout.push(Object.assign({'position':{'x': 0, 'y': 0, 'h':2, 'w':2}, 'id':  this.maxindex(),
                                    'pcolor': this.color.hex, 'hidden': false}, panel ))                                         
      }
    }
  }
}
</script>
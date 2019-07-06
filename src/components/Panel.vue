<template>
  <div class="no-drag" ref="panel">
          <Close16 class="icon" @click="Close()"/>

     <div>   
    <div v-if="panel.ptype == 'table'">
        <div v-if="result.length > 0">
          <panel-table :panel="panel" :result="result"/>
        </div>
        <div v-else>
            <cv-inline-loading :active="true" loading-text="Loading..."/>
        </div>
    </div>
    <div v-else-if="panel.ptype == 'single'">
        {{panel['title']}}
        <div class="single" >
            {{result['count']}}
        </div>
    </div>
     <div v-else-if="panel.ptype == 'chart'">
        {{panel['title']}}
        <chart :result="result"/>
    </div>
     </div>
 </div>
</template>

<script>
import io from 'socket.io-client';
import Close16 from "@carbon/icons-vue/es/close/16";
import PanelTable from "./PanelTable.vue";
import Chart from "./Chart.vue"
export default {
  name: 'panel',
  props: ['panel'],
  components: {
      Close16,
      PanelTable,
      Chart
  },
  data () {
    return {
        toggle: false,
        result: [],
    }
  },
  methods: {
    listenCount() {     
            this.$http.get('https://' + this.$store.state.dashboard.splunkhost +'/api/panel/' + this.panel.namespace)
            .then((response) => {
              console.log(response.data)
              this.result = response.data
            })
            var s = io('wss://' + this.$store.state.dashboard.splunkhost + '/' + this.panel.namespace)
            s.on('events', (data) =>{

            if (this.panel.ptype == 'table'){
                if(data.data.length > 0){
                    this.result.append(data.data)
              }
            }
           else if (this.panel.ptype == 'single'){
                this.result = data.data[0]
            }
            else if (this.panel.ptype == 'chart'){
                this.result = data.data
            }
          })
        },
        Close(){  
            this.$store.state.dashboard.layout.splice(this.$store.state.dashboard.layout.findIndex(p => p == this.panel), 1)
        }
  },
    mounted(){
        this.listenCount()
  }
}
</script>

<style>
.icon {
  position:absolute;
  top:0;
  right:0;
  cursor: pointer;
  color: rgb(51, 51, 51);
}
.single {
  position: absolute;;
  font-size: 100pt;
  top:10%;
  right:10%;
  color: rgb(51, 51, 51);
}
</style>

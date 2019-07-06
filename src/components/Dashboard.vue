<template>
<div>
<dnd-grid-container 
              :layout.sync="$store.state.dashboard.layout" 
              :bubbleUp="false"
              :margin="5"
              class="layout">
  <div v-for="panel in $store.state.dashboard.layout" :key="panel.id" >
    <dnd-grid-box :boxId="panel.id" :style="{ backgroundColor: panel.pcolor}" class="">
      <panel :panel="panel" class="table"/>
    </dnd-grid-box>
  </div>
</dnd-grid-container>
    
</div>
</template>

<script>
import Panel from './Panel.vue'
import { Container, Box } from '@dattn/dnd-grid'
import '@dattn/dnd-grid/dist/dnd-grid.css'

export default {
  name: 'dashboard',
  data(){
    return {
      eventLog: [],
    }
  },
  components: {
    Panel,
     DndGridContainer: Container,
     DndGridBox: Box
  }
}
</script>

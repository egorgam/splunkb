<template>
  <div>
    <div class="chart">
        {{result}}
      <Doughnut :data="chartData" :options="{responsive: true, maintainAspectRatio: false}"/>
    </div>
  </div>
</template>

<script>
import Doughnut from "./Doughnut.vue";
export default {
  props: ['result'],
  name: "App",
  components: { Doughnut },
  data() {
    return {
      upvotes: [1, 2, 3, 4, 5],
      chartData: {
        labels: ["Upvotes", "Shares", "Views"],
        datasets: [
          {
            backgroundColor: ["#41B883", "#E46651", "blue"],
            data: this.presult
          }
        ]
      }
    };
  },
   computed: {
    // plabels(){
    //   return this.result.map(function(item){return Object.values(item)}).slice(this.selected.start - 1, this.selected.start + this.selected.length - 1)
    // },

    presult(){
        console.log(this.result)
        // return Object.keys(this.result)
    }
  },
  methods: {
    showStats(project) {
      this.showChart = true;
      let rd = Math.floor(Math.random() * 10 + 1);
      this.chartData.datasets[0].data = [];
      this.chartData.datasets[0].data = [rd, 2, 2];
    }
  },
  mounted(){
        this.showStats()
    }
};
</script>

<style>
.chart {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

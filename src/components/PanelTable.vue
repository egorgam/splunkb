<template>
  <div ref="table">
      <data-table
              :auto-width="false"
              :sortable="true"
              row-size="short"
              :title="panel['title']"
              :zebra="true"
              :panel="panel"
              :columns="pcolumns"
              :pagination="{ numberOfItems: result.length, pageSizes: [10, 20, 50] }" 
              @pagination="actionOnPagination"
              @sort="onSort"
              :data="presult">
          </data-table>
  </div>
</template>

<script>
import DataTable from './carbon-custom/data-table'
export default {
  components:{
    DataTable
  },
  props: ['panel', 'result'],
    data () {
    return {
        selected: {'start': 1, 'length': 10},
        }
    },
 computed: {
    presult(){
      return this.result.map(function(item){return Object.values(item)}).slice(this.selected.start - 1, this.selected.start + this.selected.length - 1)
    },
    pcolumns(){
        return Object.keys(this.result[0])
    }
  },
  methods:{
    hh(){
       var header = this.$refs.table.querySelector('#header').getBoundingClientRect()
       var table = this.$refs.table.querySelector('#table').getBoundingClientRect()
       var paginator = this.$refs.table.querySelector('#paginator').getBoundingClientRect()

       var w = 210
       var h = 210

       var width = table.width
       var height = header.height + table.height + paginator.height

       this.panel.position.w = Math.ceil(((width+10)/w)*2)
       this.panel.position.h = Math.ceil((height/h)*2)
    },
        onSort(sortBy) {
            if (sortBy) {
              this.presult.sort((a, b) => {
                const itemA = a[sortBy.index];
                const itemB = b[sortBy.index];

                if (sortBy.order === "descending") {
                  if (sortBy.index === 2) {
                    return parseFloat(itemA) - parseFloat(itemB);
                  } else {
                    return itemB.localeCompare(itemA);
                  }
                }
                if (sortBy.order === "ascending") {
                  if (sortBy.index === 2) {
                    return parseFloat(itemB) - parseFloat(itemA);
                  } else {
                    return itemA.localeCompare(itemB);
                  }
                }
              })
            }
          },
      actionOnPagination(Selected){
        this.selected = Selected
      }
  },
    mounted(){
      this.hh()
      
  }

}
</script>

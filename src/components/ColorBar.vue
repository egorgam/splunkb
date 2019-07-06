<template>
  <div role="application" aria-label="Compact color picker" class="vc-compact">
    <ul class="vc-compact-colors" role="listbox">
      <li
        v-for="c in paletteUpperCase(palette)"
        role="option"
        :aria-label="'color:' + c"
        :aria-selected="c === pick"
        class="vc-compact-color-item"
        :key="c"
        :class="{'vc-compact-color-item--white': c === '#FFFFFF' }"
        :style="{background: c}"
        @click="handlerClick(c)"
      >
        <div class="vc-compact-dot" v-show="c === pick"></div>
      </li>
    </ul>
  </div>
</template>

<script>
import colorMixin from '../mixin/color'
const defaultColors = [
  '#4D4D4D', '#999999', '#F44E3B', '#FE9200', '#FCDC00', '#A4DD00', '#FFFFFF'
//   '#DBDF00', '#68CCCA', '#73D8FF', '#AEA1FF', '#FDA1FF',
//   '#333333', '#808080', '#CCCCCC', '#D33115', '#E27300', '#FCC400',
//   '#B0BC00', '#68BC00', '#16A5A5', '#009CE0', '#7B64FF', '#FA28FF',
//   '#000000', '#666666', '#B3B3B3', '#9F0500', '#C45100', '#FB9E00',
//   '#808900', '#194D33', '#0C797D', '#0062B1', '#653294', '#AB149E'
]
export default {
  name: 'Compact',
  mixins: [colorMixin],
  props: {
    palette: {
      type: Array,
      default () {
        return defaultColors
      }
    },
    dname:String
  },
  computed: {
    pick () {
      return this.colors.hex.toUpperCase()
    }
  },
  methods: {
    handlerClick (c) {
      this.$store.state.dashboard.layout.filter(p => p.dashboard == this.dname).forEach(function(panel) {
        panel.pcolor = c
      });

      this.colorChange({
        hex: c,
        source: 'hex'
      })
    }
  }
}
</script>

<style>
.vc-compact {
  padding-top: 5px;
  padding-left: 18px;
  width: 200px;
}
.vc-compact-colors {
  overflow: hidden;
  padding: 0;
  margin: 0;
}
.vc-compact-color-item {
  list-style: none;
  width: 15px;
  height: 15px;
  float: left;
  margin-right: 5px;
  margin-bottom: 5px;
  position: relative;
  cursor: pointer;
}
.vc-compact-color-item--white {
  box-shadow: inset 0 0 0 1px #ddd;
}
.vc-compact-color-item--white .vc-compact-dot {
  background: #000;
}
.vc-compact-dot {
  position: absolute;
  top: 5px;
  right: 5px;
  bottom: 5px;
  left: 5px;
  border-radius: 50%;
  opacity: 1;
  background: #fff;
}
</style>

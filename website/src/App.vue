<template>
  <div id="app">
    <Homepage/>
  </div>
</template>

<script>
import Homepage from './components/Homepage.vue'


export default {
  name: 'app',
  components: {
    Homepage
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  text-align: center;
}
</style>

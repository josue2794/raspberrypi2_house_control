<template>
  <div id="app">
    <v-toolbar color="red" >
      <v-toolbar-side-icon></v-toolbar-side-icon>
      <v-toolbar-title>Domotica</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-sm-and-down">
          <v-text-field
                  label="Password"
          ></v-text-field>
        <v-btn flat>Login</v-btn>
      </v-toolbar-items>
    </v-toolbar>
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
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>

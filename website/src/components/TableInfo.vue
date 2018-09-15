<template>
<div class="table">

  <v-data-table
          :headers="headers"
          :items="data"
          item-key="name"
          class="elevation-1"
  >
    <template slot="items" slot-scope="props">

      <td>{{ props.item.name }}</td>
      <v-alert
              :value="true"
              color="error"
              icon="warning"
              outline
      >
        This is a error alert.
      </v-alert>

    </template>
  </v-data-table>
</div>

</template>

<script>
    import axios from 'axios';

export default {
    name: 'TableInfo',
    props: {
        headers: Array,
        data: Array
    },
  data () {
    return {
        data: []
        
    }

  },
  created() {
      axios.get(`http://localhost:5555/lights`)
          .then(response => {
              this.data = response.data
          })
          .catch(e => {
              this.errors.push(e)
          })
  }

}
</script>


<style>
</style>

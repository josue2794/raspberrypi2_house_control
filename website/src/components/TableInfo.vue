<template>
<div class="table">

  <v-data-table
          :headers="headers"
          :items="items"
          item-key="name"
          class="elevation-1"
  >
    <template slot="items" slot-scope="props">

      <td>{{ props.item.name }}</td>
      <td @click="update_data()">{{props.item.value ? "Abierta" : "Cerrada"}}</td>

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
        endpoint: String,
        password: String
    },
    methods:
        {
            update_data()
            {
                axios.get(this.endpoint, {
                    headers: {
                        'Content-Type': 'application/json',
                        'password': this.password
                    }})
                    .then(response => {
                        this.items = response.data;
                    })
                    .catch(e => {
                        console.log(e)
                    })
            }
        },
  data () {
    return {
        items: []
        
    }

  },
  created() {
      this.update_data()
      setInterval(this.update_data, 1200)
  }

}
</script>


<style>
</style>

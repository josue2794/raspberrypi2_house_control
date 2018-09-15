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
        <td>{{props.item.state}}</td>

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
        data_from_api: [],
        items: this.data
        
    }

  },
  created() {
      axios.get(`http://localhost:5555/doors`)
          .then(response => {
              this.data_from_api = response.data
              let i;
              for (i = 0; i < this.items.length; i++) {
                  if(this.data_from_api.hasOwnProperty(this.items[i].id))
                  {
                      this.items[i]['state'] = this.data_from_api[this.items[i].id];
                  }
              }
          })
          .catch(e => {
              console.log(e)
          })
  }

}
</script>


<style>
</style>

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
      <v-switch v-model="props.item.value" v-on:change="switching(props.item)" color="red"></v-switch>

    </template>
  </v-data-table>
</div>

</template>

<script>
    import axios from 'axios';


export default {
    name: 'Table',
    props: {
        headers: Array,
        endpoint: String,
        password: String
    },
    methods:
        {
            switching(switche) {
                axios.post(this.endpoint, switche,  {
                    headers: {
                        'Content-Type': 'application/json',
                        'password': this.password
                    }})
                    .then(response => {
                        this.update_data()
                    })
                    .catch(e => {
                        console.log(e)
                    })

            },
            update_data()
            {
                axios.get(this.endpoint,{
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
                this.update_data();
          }

}
</script>


<style>
</style>

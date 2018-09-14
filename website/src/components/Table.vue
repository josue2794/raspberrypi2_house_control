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
      <v-switch v-model="selected" color="red" label="State" value="props.item.id"></v-switch>

    </template>
  </v-data-table>
</div>

</template>

<script>


export default {
    name: 'Table',
    props: {
        headers: Array,
        data: Array
    },
  data () {
    return {
        selected: []
        
    }
}

}
</script>


<style>
</style>

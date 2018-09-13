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
  data () {
    return {
        headers: [
          {
            text: 'Habitación',
              align: 'left',
            value: 'name'
          },
          { text: 'Luz', value: 'id' }
        ],
        data: [
        { value: false, name: 'Sala', id: 0},
        { value: false, name: 'Comedor', id: 1},
        { value: false, name: 'Habitación principal', id:2},
        { value: false, name: 'Habitación niños', id: 3}
        ],
        selected: []
        
    }
  }
 
}
</script>


<style>
</style>

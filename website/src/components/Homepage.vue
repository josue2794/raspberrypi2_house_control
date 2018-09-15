<template>
  <div class="Homepage">
      <Table :headers="luz_headers" :data="luz_data" />
      <TableInfo :headers="puerta_headers" :data="puerta_data"/>
  </div>
</template>


<script>
import Table from './Table.vue'
import TableInfo from "./TableInfo";

const luz_headers = [
        {
            text: 'Habitación',
            align: 'left',
            value: 'name'
        },
        { text: 'Luz', value: 'id' }
        ]
const luz_data = [
        { value: false, name: 'Sala', id: 0, state:0},
        { value: false, name: 'Comedor', id: 1, state:0},
        { value: false, name: 'Habitación principal', id:2, state:0},
        { value: false, name: 'Habitación niños', id: 3, state:0}
        ]

const puerta_headers = [
    {
        text: 'Puerta de Habitacion',
        align: 'left',
        value: 'name'
    },
    { text: 'Estado', value: 'id' }
]
const puerta_data = [
    { value: false, name: 'Sala', id: 0, state:0},
    { value: false, name: 'Comedor', id: 1, state:0},
    { value: false, name: 'Habitación principal', id:2, state:0},
    { value: false, name: 'Habitación niños', id: 3, state:0}
]


export default {
  name: 'Homepage',
  components: {
      TableInfo,
    Table
  },
    data () {
        return {
            luz_data: luz_data,
            luz_headers: luz_headers,
            puerta_data: puerta_data,
            puerta_headers: puerta_headers

        }

        }
}
</script>

<style scoped>

</style>

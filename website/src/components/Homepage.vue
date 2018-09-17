<template>
  <div class="Homepage">
      <v-toolbar color="red" >
          <v-toolbar-side-icon></v-toolbar-side-icon>
          <v-toolbar-title>Domotica</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-toolbar-items class="hidden-sm-and-down">
              <v-text-field v-if="!authenticated" v-model="password" type="password"
                            label="Password"
              ></v-text-field>

              <v-btn v-if="!authenticated" @click="login" flat>Login</v-btn>

          </v-toolbar-items>
          <td v-if="error">Error Authenticating</td>
          <v-toolbar-title v-if="authenticated">Hello Admin</v-toolbar-title>
      </v-toolbar>
      <Table v-if="authenticated" :headers="luz_headers" :endpoint="luz_endpoint" :password="password"/>
      <TableInfo v-if="authenticated" :headers="puerta_headers" :endpoint="puerta_endpoint" :password="password"/>
  </div>
</template>


<script>
import Table from './Table.vue'
import TableInfo from "./TableInfo";
import axios from 'axios';

const luz_headers = [
        {
            text: 'Habitación',
            align: 'left',
            value: 'name'
        },
        { text: 'Luz', value: 'id' }
        ]
const endpoint = 'http://localhost:5555'
const luz_endpoint = endpoint + '/lights'
const puerta_endpoint = endpoint +'/doors'
const puerta_headers = [
    {
        text: 'Puerta de Habitacion',
        align: 'left',
        value: 'name'
    },
    { text: 'Estado', value: 'id' }
]

export default {
  name: 'Homepage',
  components: {
      TableInfo,
    Table
  },
    methods : {
      login() {
        axios.post(endpoint+ '/auth',{}, {
            headers: {
                'Content-Type': 'application/json',
                'password': this.password
            }})
            .then(response => {
                let status = response.status;
                if (status == 200) {
                    this.authenticated = true
                    this.error = false
                }
                else
                    this.error = true
            })
            .catch(e => {
                this.error = true
            })

      }

    },
    data () {
        return {
            luz_headers: luz_headers,
            puerta_headers: puerta_headers,
            luz_endpoint: luz_endpoint,
            puerta_endpoint: puerta_endpoint,
            password: "",
            authenticated: false,
            error: false
        }

    }

}
</script>

<style scoped>

</style>

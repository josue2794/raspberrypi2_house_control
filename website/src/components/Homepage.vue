<template>
    <div justify-center>
        <v-toolbar color="red">
            <v-toolbar-title>Domotica</v-toolbar-title>
            <v-spacer></v-spacer>
                <v-text-field v-if="!authenticated" v-model="password" type="password"
                              label="Password"
                ></v-text-field>

                <v-btn v-if="!authenticated" @click="login" flat>Login</v-btn>
            <td v-if="error">Error Authenticating</td>
            <v-toolbar-title v-if="authenticated">Hello Admin</v-toolbar-title>
        </v-toolbar>
        <v-subheader  v-if="authenticated">Lights</v-subheader>
        <Table v-if="authenticated" :headers="luz_headers" :endpoint="luz_endpoint" :password="password"/>
        <v-subheader  v-if="authenticated"> Doors</v-subheader>
        <TableInfo v-if="authenticated" :headers="puerta_headers" :endpoint="puerta_endpoint" :password="password"/>
        <v-spacer></v-spacer>
        <v-subheader  v-if="authenticated"> Camera Picture</v-subheader>
        <v-card @click="update_img()" primary-title><v-img  v-if="authenticated" :src="img_endpoint" class="grey darken-4"></v-img></v-card>
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
        {text: 'Luz', value: 'id'}
    ]
    const endpoint = 'http://192.168.100.17:5555';
    const luz_endpoint = endpoint + '/lights';
    const puerta_endpoint = endpoint + '/doors';
    const img_endpoint = endpoint + '/img';
    const puerta_headers = [
        {
            text: 'Puerta de Habitacion',
            align: 'left',
            value: 'name'
        },
        {text: 'Estado', value: 'id'}
    ]

    export default {
        name: 'Homepage',
        components: {
            TableInfo,
            Table
        },
        methods: {
            login() {
                axios.post(endpoint + '/auth', {}, {
                    headers: {
                        'Content-Type': 'application/json',
                        'password': this.password
                    }
                })
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

            },
            update_img() {
                if(this.authenticated) {
                    this.img_endpoint = endpoint + "/img?" + new Date().getTime()
                }
            },

        },
        data() {
            return {
                luz_headers: luz_headers,
                puerta_headers: puerta_headers,
                luz_endpoint: luz_endpoint,
                puerta_endpoint: puerta_endpoint,
                img_endpoint: img_endpoint,
                password: "",
                authenticated: false,
                error: false,
                img_show: false
            }

        },
        created() {
            this.update_img()
            setInterval(this.update_img, 7000)
        }

    }
</script>

<style scoped>

</style>

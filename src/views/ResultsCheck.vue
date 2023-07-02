<script setup lang="ts">
// Access store to get out user information
import { useUserStore } from '@/stores/user'
import { ref, reactive } from 'vue'
import axios from 'axios'
const store = useUserStore()
// Get username from store
const username = ref(store.username)
console.log(username.value)
// Get name from store
const name = ref(store.name)
// Get candidate number from store
const candidateNumber = ref(store.candidateNumber)
// Get centre from store
const centre = ref(store.centre)
// The result
const result = reactive({})
// First check whether the user have logged in
if (username.value == null || name.value == null){
    window.location.replace('/')
    console.log('Proceed to the main page')
}else{
    // Send information to the server to get results
    axios({
    method: 'post',
    url: 'http://localhost:5000/results',
    data: {
        username: username.value
    }
    })
    .then(function(response){
        console.log(response.data);
        // To make my life easier, I bypassed CORS by just accepting a string. Thus I need to change it to JSON.
        const modifiedData = response.data.replace(/ObjectId\('[^']+'\)/g, 'null').replace(/'/g, '"');
        const parsedData = JSON.parse(modifiedData);
        console.log(parsedData)
        Object.assign(result, parsedData.results)
    });
}
</script>
<template>
    <div style="margin: 20px 15px; font-size: 20px;"> Dear {{ name }}, please check that your personal details are correct, and then check the results below. </div>
    <div id="userInfo">
        
        Name: {{ name }} <br>
        Username: {{ username }} <br>
        Candidate Number: {{ candidateNumber }} <br>
        Centre: {{ centre }}
    </div>
    <div id="results" v-for = "(item, key) in result">
        {{ key }}
        <table>
            <thead>
                <tr>
                    <th> Subject </th>
                    <th> Score </th>
                </tr>
            </thead>
            <tbody v-for = "(marks, subject) in item">
                <tr>
                    <td> {{ subject }} </td>
                    <td> {{ marks }} </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>
  
<style>
*{
    margin:0;
    padding:0;
    background-color:black;
    font-family: Rubik;
    color: white;
}
#userInfo{
    text-align: left;
    margin-top: 50px;
    margin-left: 30px;
    font-size: 25px;
    font-weight: bold;
}
#results{
    text-align: center;
    margin-top: 25px;
    font-size: 30px;
}
table{
    margin-left: auto;
    margin-right: auto
}
table, td{
    font-size: 25px;
    border: 1px solid white;
}
</style>
  
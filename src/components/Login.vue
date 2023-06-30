<script setup lang="ts">
import { reactive, ref } from 'vue'
import Login from '../components/Login.vue'
import { sha256 } from 'js-sha256'
import axios from 'axios'
// Since we declared the two values as null, we need to pre-declare the type of the two values by using interface
interface UserDetailsType{
    username: String | null
    password: String | null
}
const userDetails: UserDetailsType = reactive({ username: null, password: null})
const message = ref()
function sendData(){
    if (userDetails.username == null || userDetails.password==null){
        message.value = "Please enter your login detail."
    }else{
        // Send information to the server
        axios({
            method: 'post',
            url: 'http://localhost:5000/login',
            data: {
                username: userDetails.username.toString(), 	// user input from form
                password: sha256(userDetails.password.toString())	// sha256 of user input from form
            }
        })
            .then(function(response){
                if(response.data.passed == True){
                    console.log("redirect")
                }
            })
    }
}
</script>

<template>
  <main>
    <!-- The Login Box -->
    <div class="LoginBox">
        <h2>Online Results Checking Service</h2>
        <!-- The Login Form -->
        <form id="Login">
            <input type="text" placeholder=" Username" class="InputBoxes" v-model="userDetails.username"> <br>
            <input type="text" placeholder=" Password" class="InputBoxes" v-model="userDetails.password"> <br>
            {{ message }}
            <div id="Submit" @click="sendData()">Submit</div>
        </form>
    </div>
  </main>
</template>

<style>
@font-face {
    font-family: Rubik;
    src: url(../assets/Rubik-VariableFont_wght.ttf)
}
*{
    margin:0;
    padding:0;
    background-color:black;
    font-family: Rubik;
}
.LoginBox{
    width:100%;
    height:250px;
    background-color:rgb(35, 35, 35);
    top: 50%;
    margin-top:-125px;
    position:absolute;
    color:white;
    text-align:center;
}
#Login{
    background-color:rgb(35, 35, 35);
}
.InputBoxes{
    width:400px;
    height:30px;
    border-radius:10px;
    color:white;
    position:relative;
    margin-top:30px;
    border-color:grey
}
#Submit{
    width:100px;
    height:30px;
    text-align:center;
    margin-left:auto;
    margin-right:auto;
    margin-top:30px;
    padding-top:5px;
    position:relative;
    border-radius: 10px;
    font-size: 20px;
}
#Submit:hover{
    animation-name: buttonFade;
    animation-duration: 1s;
}
/* Keyframe animation of the button when hover */
@keyframes buttonFade{ 
    from {background-color: black; color: white;}
    to {background-color: white; color:black;}
}
</style>

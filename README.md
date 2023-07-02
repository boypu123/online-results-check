# Online Results Check

This is an online results query service template. Built using Vue 3 + Typescript + Pinia + Vue Router 4 + Flask + MongoDB

You are free to copy and use this template. You can change this template as well, as long as you indicate the original author (For example, paste the github link of this work to the website that you are going to post your modified work).

server.py is the server file, built using flask.
admin.py is the admin panel. You can use this, however, it is recommended that you follow the basic code

May I remind you that this source code itself is **NOT PRODUCTION READY**. To make it production ready, refer to this site: https://flask.palletsprojects.com/en/2.1.x/tutorial/deploy/
## Install
Clone this respository from github. 
You can also download the source code and put it somewhere in your computer.
You also need to install python. I used python 3.11 while writing this piece of code. It is recommended that you download the same version of python as me.
Then, you need to run the following:
``
pip install pymongo
``
``
pip install flask
``
``
pip install flask-cors
``
You also need to install MongoDB. You can download it here, on their official website: https://www.mongodb.com/download-center/community/releases
After installing it, connect it and create a database called ``results_query``, with 

Don't forget to download node.js! https://nodejs.org/en/download

That should be all the things that you need to install.
## Run
Run this code:
``
npm run dev
``
and run server.py.
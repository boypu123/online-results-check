# Online Results Check
![image](https://github.com/boypu123/online-results-check/assets/62825102/90a8342d-5267-4a7b-847e-bb1effb2d02d)


This is an online results query service template. Built using Vue 3 + Typescript + Pinia + Vue Router 4 + Flask + MongoDB

You are free to copy and use this template. You can change this template as well, as long as you indicate the original author (For example, paste the GitHub link of this work to the website where you are going to post your modified work).

server.py is the server file, built using Flask.
admin.py is the admin panel. You can use this, however, it is recommended that you follow the basic code and create your own admin panel.

May I remind you that this source code itself is **NOT PRODUCTION READY**. To make it production ready, refer to this site: https://flask.palletsprojects.com/en/2.1.x/tutorial/deploy/

## Key Features
 - Can add multiple qualifications
 - Can add candidate number and centre name
 - Display the results in a table format
 - Quick responding speed
 - Password encryption

## Install
Clone this repository from GitHub. 
You can also download the source code and put it somewhere on your computer.
You also need to install python. I used Python 3.11 while writing this piece of code. It is recommended that you download the same version of Python as me.
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

Don't forget to download node.js! https://nodejs.org/en/download

Then you need to run start.py to do some initialisation work.

That should be all the things that you need to install.

## Run
Run this code:
``
npm run dev
``
and run server.py just like how you run a normal Python file.

## Reminders
Sometimes the port of the node.js server may not be 5174. In this case, go to server.py, modify every http://localhost:5173 to http://localhost:{insert the port where node.js server is running here}

## Future Plans
Add i18n support maybe.

Have any more questions?
Email me @:
boypu9673@gmail.com
boypu123@outlook.com

WeChat me @:
boypu123

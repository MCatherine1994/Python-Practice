### **This is a simple start tutorial to introduce the steps to run the BattleSnake 2018 Server and the ideas to improve the proformance**  
##### All the python program here are drafts, for more information about the python program and the complete version, please see the [BattleSnake Project](https://github.com/BATSnake/battlesnake-python) in the organization. That is a beginner semi-final level snake. 
  
### **Introduction**
Information about the BattleSnake competition, please see the the officail website: https://www.battlesnake.io/.  
All the following steps are working on the 2018 BattleSanke Server. Server for each year maybe different. Please read the full instrunction from [sendwithus](https://github.com/sendwithus). For the full document for 2018, see from [here](https://github.com/sendwithus/battlesnake). Please follow the instruction from sendwithus first, cause you need to fork the project from them, and this document will just share some experience. Please do not relay on this document.  
  
### **Run your snake locally**  
#### **You need...**  
* a working Python 2.7 development environment ([getting started guide](http://hackercodex.com/guide/python-development-environment-on-mac-osx/))
* experience [deploying Python apps to Heroku](https://devcenter.heroku.com/articles/getting-started-with-python#introduction)---this one is for deploying your project so that other authentication part can run your code. You will need this for the competition.
* [pip](https://pip.pypa.io/en/latest/installing.html) to install Python dependencies  

#### **Steps:**  
1) [Fork this repo](https://github.com/sendwithus/battlesnake-python/fork). (Fork from official site please, and be careful the year.)  

2) Clone repo to your development environment: (This step is cloneing a local version of your project.)  
```
git clone git@github.com:username/battlesnake-python.git
```

3) Install dependencies using [pip](https://pip.pypa.io/en/latest/installing.html):
```
pip install -r requirements.txt
```

4) Run local server:
```
python app/main.py
```
5) Test client in your browser: [http://localhost:8080](http://localhost:8080)

#### **Now you want to test your snake on the server:** (This is for mac, for windows please see the instruction from offical site)
1) [Install Docker](https://docs.docker.com/install/)

2) Run: docker pull sendwithus/battlesnake-server 
This is to update the server to the latest version  

3) Run: docker run -it --rm -p 3000:3000 sendwithus/battlesnake-server  
Start the server  

4) Visit: http://localhost:3000/, then you will see the front page to allow you create a new game

5) The URL for your snake is http://[you local ip addrss]:8080, remember to enter a name fieldd just next to url field (if you forget to enter the name, your snake will only move one step). You could find out your local ip address by typing "ifconfig" at the terminal. "8080" here is the port number, which you could change in your code.    

6) Now you are ready to test your snake  
  
  
### **Deploy your sanke to Heroku**  
##### You need to do this so that other authentication part(like sendwithus) can run your snake  
1) Create a new Heroku app:
```
heroku create [APP_NAME]
```

2) Deploy code to Heroku servers:
```
git push heroku master
```

3) Open Heroku app in browser:
```
heroku open
```
or visit [http://APP_NAME.herokuapp.com](http://APP_NAME.herokuapp.com).

4) View server logs with the `heroku logs` command:
```
heroku logs --tail
```
Read the Heroku tutorial in the previous (You need...) section  
  
  
### **The following part will introduce the ideas of our snake and what need to improve**  
#### **Steps of how we build our snake:**  
1) Run and test the server to see how the board looks like and how the snake suppose to move.  
2) Read the tutorial of [bottle web framework](http://bottlepy.org/docs/dev/index.html) and try to understand how it works.  
3) After know how our program is going to respone the server request, now it is the time to think of the algorithm.  
   **Our goals to achieve:**  
   a. Read all information provided in the server request (eg. snake id, position, health, length and food position)  
   b. Let the snake won't go through the wall  
   c. Let the snake eat food  
   d. Let the snake won't eat itself (This is not easy to achieve when the snake grows bigger)  
   e. Forcast the movements  
   f. Assign security value to each grid and let the snake move based on security level  
4) Create severl lists to store the snake information and food information  
5) Create a board to store position information and assign different value based on what is in the grid and what is going to be in the grid  
6) Create a method to define the way the snake move, track the location of the snake and let it turns around when it comes to the wall  
7) Assign security level by forcast the next 5 round move (This method takes time and need to be improved)  
  
#### **What needs to improve:**  
1) Design a proper self loop method and let the snake move towards it tail  
2) Apply different strategy during different stage (eg. At the very begining, try to eat food. When the health value is high enough, maybe could do the self loop to protect ourself. And when there is a snake coming close, move to a safe plave. When the length is long enough, try to cut other snake's trail)  
  
#### **Problems encountered:**  
We have a quite perfect idea to calculate the route of our sanke using BFS, and we do have the draft code. But the program using BFS takes a really long time that we can not sure if we could send response back in the certain amount time.  
Even the method we currently use has the same problem. When we are trying to forcast the next 10 round movemnet for all snake, it will take a long time, which is not what we expected.

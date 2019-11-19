# Heroku-Flask-ModelV1
 <br/>
This repository holds the key to create a rest service on Heroku platform. This will deployed to Heroku using the Docker.


# Build Docker Image
 <br/>
docker build -t flask-model:latest .

# deploy to Heroku Via Docker "flaskrestmodel" is the name of the app registed on the heroku 
<br/> <br/>
heroku login <br/>
heroku container:login <br/>
heroku container:push web --app flaskrestmodel <br/>
heroku container:release web --app flaskrestmodel <br/>
heroku open --app flaskrestmodel

# endpoints
<h2> Cureenlty this app is deployed on https://flaskrestmodel.herokuapp.com/ so all the endpoints are related to this.

<ul>
 <li>
  <b>/</b> : Prints Hello World
  </li>
 
 
 <li>
 <b> /<name> </b>: Prints Hello <name>
  </li>
 
 
 <li>
  <b>/todo/model </b>: Retrieve the cluster assigned to the WholesSales
  </li>
  
  <li>
  <b>/todo/contactModel </b>: Retrieve the cluster assigned to the contact
  </li>
  
   <li>
  <b>/todo/traincontactModel/<number> </b>: Train the contact model with given number of clusters
  </li>
 
  <li>
  <b>/todo/trainWhModel/<number> </b>: Train the wholesale model with given number of clusters
  </li>
 <ul>

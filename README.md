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

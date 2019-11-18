# Heroku-Flask-ModelV1
This repository holds the key to create a rest service on Heroku platform. This will deployed to Heroku using the Docker.


# Build Docker Image
docker build -t flask-model:latest .

# deploy to Heroku Via Docker "flaskrestmodel" is the name of the app registed on the heroku
heroku login
heroku container:login
heroku container:push web --app flaskrestmodel
heroku container:release web --app flaskrestmodel
heroku open --app flaskrestmodel

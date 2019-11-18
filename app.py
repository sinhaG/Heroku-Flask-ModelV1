from flask import Flask, request, jsonify
from service import ToDoService
from models import Schema
import os
from service import model,modelContact
import json

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] =  "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, DELETE, OPTIONS"
    return response


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/<name>")
def hello_name(name):
    return "Hello " + name


@app.route("/todo", methods=["GET"])
def list_todo():
    return jsonify(ToDoService().list())


@app.route("/todo", methods=["POST"])
def create_todo():
    return jsonify(ToDoService().create(request.get_json()))


@app.route("/todo/<item_id>", methods=["PUT"])
def update_item(item_id):
    return jsonify(ToDoService().update(item_id, request.get_json()))


@app.route("/todo/<item_id>", methods=["DELETE"])
def delete_item(item_id):
    return jsonify(ToDoService().delete(item_id))

@app.route("/todo/model", methods=["POST"])
def clustering():
    return jsonify(model(request.get_json()))


@app.route("/todo/contactModel", methods=["POST"])
def clustering_contact():
    return jsonify(modelContact(request.get_json()))

if __name__ == "__main__":
    Schema()
    app.run(debug=True, host='0.0.0.0',port=port)
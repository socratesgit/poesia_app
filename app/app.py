import json
import os
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson import json_util


application = Flask(__name__)

application.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']

mongo = PyMongo(application)
db = mongo.db

def parse_json(data) -> dict:
    return json.loads(json_util.dumps(data))


@application.route('/')
def index():
    return jsonify(
        status=True,
        message='Hai raggiunto il sito di Poesia Errante!'
    )

@application.route('/poems')
def poems():
    poems = db.poems.find()
    return jsonify(
        status=True,
        data=parse_json(poems)
    )

@application.route('/poems/<author>')
def poems_by_author(author):
    poems = db.poems.find({'author':
        author
    })
    return jsonify(
        status=True,
        data=parse_json(poems)
    )

@application.route('/poems', methods=['POST'])
def create_poem():
    poem = {
        'title': request.json['title'],
        'author': request.json['author'],
        'text': request.json['text']
    }
    db.poems.insert_one(poem)
    return jsonify(
        status=True,
        message='Poem created successfully!'
    )

if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    application.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
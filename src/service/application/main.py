import math
import random
import logging
import json
from flask_cors import CORS


from flask import Flask, jsonify, request
import os

PORT = int(os.environ.get('PORT', 5000))
DEBUG_STR = os.environ.get('DEBUG', 'false')

if DEBUG_STR.lower() == 'true':
    DEBUG = True
else:
    DEBUG = False

app = Flask(__name__)
CORS(app)

objects = {}

@app.route('/ping', methods=['GET'])
def ping():
    return 'pong'

@app.route('/objects', methods=['GET'])
def get_objects():
    """
    Retrieve a list of objects
    :return: JSON Object.
    """
    logging.info('Returning list of objects')
    object_ids = []

    for k,v in objects.items():
        object_ids.append(k)

    return jsonify({
        'status': 'ok',
        'task': 'list',
        'objects': object_ids
    })


@app.route('/objects/<objectId>', methods=['GET'])
def get_object(objectId):
    """
    Retrieve a single object.
    :return: JSON
    """
    logging.info('Returning single object for id {}'.format(objectId))

    print(objectId)

    print(objects.get(objectId))
    print(objects)

    return jsonify({
        'status': 'ok',
        'task': 'single',
        'object': objects.get(objectId, None)
    })


@app.route('/objects', methods=['POST'])
def add_object():
    """
    Add a new object to the dict.
    :return: JSON
    """
    obj = json.loads(request.get_data())
    objectId = _get_random_id()
    obj['id'] = objectId

    objects[str(objectId)] = obj

    return jsonify({
        'status': 'ok',
        'task': 'create',
        'id': objectId
    })


@app.route('/objects/<objectId>', methods=['PUT'])
def update_object(objectId):
    """
    Update an object
    :param objectId: ID to update
    :return: JSON
    """
    try:
        obj = request.get_json()
        objects[objectId] = obj

    except Exception as E:
        logging.error("ERROR: Couldn't find ID to update")

    return jsonify({
        'status': 'ok',
        'task': 'update'
    })


@app.route('/objects/<objectId>', methods=['DELETE'])
def delete_object(objectId):
    """
    Delete an object.
    :param objectId: ID to delete
    :return: JSON
    """
    try:
        objects.pop(objectId)
    except Exception as E:
        logging.error("ERROR: Couldn't find ID to remove")

    return jsonify({
        'status': 'ok',
        'task': 'delete'
    })


def _get_random_id():
    return random.randint(1, 9999999)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=DEBUG)

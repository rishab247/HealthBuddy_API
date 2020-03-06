from flask import Flask, jsonify, request, make_response, logging
import json


app = Flask(__name__)


@app.route('/Askme', methods=['POST'])
def Askme():
    data = request.get_data().decode("utf-8")
    data = json.loads(data)
    print(data)
    return jsonify({'msg': 'FUCK OFF'}), 200


@app.route('/', methods=['GET'])
def Askme1():

    return jsonify({'msg': 'FUCK OFF'}), 200


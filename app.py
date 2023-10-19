from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch
import json

# Elasticsearch connection
es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])

# Define the Elasticsearch index name
index_name = 'application_status'

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    try:
        if 'file' not in request.files:
            return "No file part", 400
        file = request.files['file']
        if file.filename == '':
            return "No selected file", 400
        if file:
            data = file.read()
            data = json.loads(data.decode('utf-8'))
            es.index(index=index_name, body=data)
            return "Data added to Elasticsearch", 201
    except Exception as e:
        return str(e), 500

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    pass

@app.route('/healthcheck/<service_name>', methods=['GET'])
def healthcheck_by_service():
    pass

if __name__ == '__main__':
    app.run()
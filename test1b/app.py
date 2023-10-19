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
    try:
        result = es.search(index=index_name, size=10000)
        hits = result['hits']['hits']
        application_statuses = []
        for hit in hits:
            application_statuses.append(hit['_source'])
        return jsonify(application_statuses)
    except Exception as e:
        return str(e), 500

@app.route('/healthcheck/<service_name>', methods=['GET'])
def healthcheck_by_service(service_name):
    try:
        result = es.search(index=index_name, body={"query": {"match": {"service_name": service_name}}})
        hits = result['hits']['hits']
        application_statuses = []
        for hit in hits:
            application_statuses.append(hit['_source'])
        return jsonify(application_statuses)
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run()
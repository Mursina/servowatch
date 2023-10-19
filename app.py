from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch

# Elasticsearch connection
es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])

# Define the Elasticsearch index name
index_name = 'application_status'

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    pass

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    pass

@app.route('/healthcheck/<service_name>', methods=['GET'])
def healthcheck_by_service():
    pass

if __name__ == '__main__':
    app.run()
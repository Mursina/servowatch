from flask import Flask, request, jsonify

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
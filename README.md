# servowatch
A simple project about monitoring the services


## Project Setup

### Version
python 3.10+

### Create a virtual environment

Create,

```
python3.10 -m venv penv
```

Activate,
```
. penv/bin/activate
```

### Install python packages

```
pip install -r requirements.txt
```

## Test 1 a)

### Run the script

```
python -m monitor_service
```

## Test 1 b)

### Run the flask application
```
python -m app
```

### Elasticsearch Configuration

Installation guide is available [here](https://www.elastic.co/guide/en/elasticsearch/reference/8.10/install-elasticsearch.html)

Access elasticsearch via http://localhost:9200

**Note**: the postman collection is available in the same repo with the name Servowatch.postman_collection.json


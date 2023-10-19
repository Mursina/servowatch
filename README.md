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
python -m test1a.monitor_services
```

## Test 1 b)

### Run the flask application
```
python -m test1b.app
```

### Elasticsearch Configuration

Installation guide is available [here](https://www.elastic.co/guide/en/elasticsearch/reference/8.10/install-elasticsearch.html)

Access elasticsearch via http://localhost:9200

**Note**: the postman collection is available in the same repo with the name test1b/Servowatch.postman_collection.json

## Test 2

If the user is secured with password, then pass the password while running the ansible command like below,

```
ansible-playbook --ask-become-pass assignment.yml -i inventory -e action=verify_install
```

## Test 3

```
Input file: test3/sales_data.csv
Output file: test3/filtered-sales-data.csv
```


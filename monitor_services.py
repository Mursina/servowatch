import psutil
import os
import time
import json

services = ['httpd', 'postgres']

# Get the host name
host_name = os.uname().nodename

for service in services:
    service_status = "DOWN"
    
    # Check the status of each service
    for process in psutil.process_iter(attrs=['name']): 
        if service in process.info['name']:
            service_status = "UP"
            break
    
    status_obj = {
        "service_name":service,
        "service_status":service_status,
        "host_name":host_name
    }

    # Generate timestamp
    time_stamp = time.strftime('%Y%m%d%H%M%S')

    # Write the JSON status object to file
    file_name = f'{service}-{service_status}-{time_stamp}.json'
    with open(file_name, 'w') as json_file:
        json.dump(status_obj, json_file, indent=4)
    
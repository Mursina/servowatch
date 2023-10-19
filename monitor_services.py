import psutil
import os

services = ['httpd', 'postgres']
status = []

host_name = os.uname().nodename

for service in services:

    service_status = "DOWN"
    
    for process in psutil.process_iter(attrs=['name']): 
        if service in process.info['name']:
            service_status = "UP"
            break
    
    status_obj = {
        "service_name":service,
        "service_status":service_status,
        "host_name":host_name
    }
    status.append(status_obj)

print(status)
import psutil

services = ['httpd', 'postgres']
status = []

for service in services:
    status_obj = {
        "service_name":service,
        "service_status":"DOWN",
        "host_name":"host1"
    }
    
    for process in psutil.process_iter(attrs=['name']): 
        if service in process.info['name']:
            status_obj ={
                "service_name":service,
                "service_status":"UP",
                "host_name":"host1"
            }
            break

    status.append(status_obj)
print(status)
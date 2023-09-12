import boto3
import json

session = boto3.Session()

# Get all available services in boto3
available_services = session.get_available_services()

# Dictionary to store services and their 'list' or 'describe' methods
service_methods = {}

# Loop through each service to find its 'list' or 'describe' methods
for service in available_services:
    client = session.client(service)
    methods = [method for method in dir(client) if 'list_' in method or 'describe_' in method]
    service_methods[service] = methods

with open('aws_services_and_methods.json', 'w') as f:
    json.dump(service_methods, f, indent=4)

print("AWS services and their 'list' or 'describe' methods have been saved to aws_services_and_methods.json")

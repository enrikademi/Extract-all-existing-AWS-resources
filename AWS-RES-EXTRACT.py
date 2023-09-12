import boto3
import json
from datetime import datetime

# Custom serialization function to handle datetime objects
def serialize_datetime(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()

# Input AWS credentials from the user
aws_access_key_id = input("Enter your AWS access key ID: ")
aws_secret_access_key = input("Enter your AWS secret access key: ")

# Initialize AWS SDK with provided credentials
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

# Input desired regions from the user
regions_input = input("Enter desired AWS regions (comma-separated): ")
aws_regions = [region.strip() for region in regions_input.split(',')]


client_name = input("Enter your client's name: ")

# Initialize a dictionary to store resource data
aws_data = {}


with open('aws_services_methods.json', 'r') as config_file:
    service_methods = json.load(config_file)

# Iterate through AWS regions
for aws_region in aws_regions:
    region_data = {}  # Store data specific to this region

    # Iterate through services and their API methods
    for service, methods in service_methods.items():
        service_data = {}  # Store data specific to this service

        try:
            client = session.client(service, region_name=aws_region)

            for method in methods:
                try:
                    response = getattr(client, method)()
                    service_data[method] = response
                except Exception as e:
                    pass  # Ignore errors and continue

            region_data[service] = service_data
        except Exception as e:
            pass  # Ignore errors and continue

    aws_data[aws_region] = region_data

output_filename = 'details_infos_aws_resources.json'
with open(output_filename, 'w') as json_file:
    json.dump(aws_data, json_file, default=serialize_datetime, indent=4)

print(f"AWS resources and configurations exported to {output_filename}")
print(f"These are the {client_name} outputs")

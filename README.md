# Extract-all-existing-AWS-resources

# AWS Resource Listing Tool
This is a Python script that allows you to list AWS resources across multiple AWS regions. It dynamically fetches the available AWS services and their associated methods and then queries each service for resource information in the specified AWS regions. The collected data is saved to a JSON file.

# Prerequisites
Before using this tool, ensure that you have the following prerequisites installed:

Python 3.x
Boto3 library (pip install boto3)
AWS CLI configured with necessary credentials
# Usage
Clone this repository to your local machine.

Open a terminal and navigate to the project directory.

Run the script by executing the following command:

bash
Copy code
python aws_resource_listing.py
You will be prompted to enter your AWS access key ID, secret access key, the desired AWS regions (comma-separated), and your client's name. Follow the on-screen instructions.

The script will start querying AWS services in the specified regions. The data will be collected and saved to a JSON file named client_name_aws_resources.json, where client_name is the name you provided.

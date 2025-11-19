import boto3

# Create a boto3 session
aws_management_console = boto3.session.Session()

# EC2 client
aws_management_client = aws_management_console.client(
    service_name="ec2",
    region_name="us-east-1",
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test"
)

# Describe instance statuses
response = aws_management_client.describe_instance_status()["InstanceStatuses"]

for instance in response:
    instance_id = instance.get("InstanceId")
    availability_zone = instance.get("AvailabilityZone")  # Corrected key
    instance_state = instance.get("InstanceState", {}).get("Name")
    instance_status = instance.get("InstanceStatus", {}).get("Status")
    system_status = instance.get("SystemStatus", {}).get("Status")

    print(f"Instance ID: {instance_id}")
    print(f"Availability Zone: {availability_zone}")
    print(f"State: {instance_state}")
    print(f"Instance Status: {instance_status}")
    print(f"System Status: {system_status}")
    print("-" * 40)

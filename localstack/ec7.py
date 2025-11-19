import boto3

# Create a boto3 session
aws_management_console = boto3.session.Session()

# EC2 resource
aws_management_resource = aws_management_console.resource(
    service_name="ec2",
    region_name="us-east-1",  # Corrected region name
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test"
)

# EC2 client
aws_management_client = aws_management_console.client(
    service_name="ec2",
    region_name="us-east-1",
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test"
)

# Stop specific instances
response = aws_management_client.stop_instances(
    InstanceIds=[
        'i-6dcf09a05744c90d7',
        'i-22df23432e803a075',
        'i-d5f51e2b02fcf78bc'
    ]
)

for  each_volume in aws_management_resourc.volume.all():
    print(each_volume.id , each_volume.state)
    


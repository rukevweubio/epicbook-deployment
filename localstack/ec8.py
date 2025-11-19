import boto3
import time

# Create a boto3 session
session = boto3.session.Session()

# EC2 client and resource pointing to LocalStack
ec2_client = session.client(
    service_name="ec2",
    region_name="us-east-1",
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test"
)

ec2_resource = session.resource(
    service_name="ec2",
    region_name="us-east-1",
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test"
)

# 1. Create VPC
vpc = ec2_resource.create_vpc(CidrBlock='10.0.0.0/16')
vpc.wait_until_available()
vpc.create_tags(Tags=[{"Key": "Name", "Value": "MyVPC"}])
print(f"Created VPC: {vpc.id}")

# 2. Create Subnet
subnet = ec2_resource.create_subnet(
    CidrBlock='10.0.1.0/24',
    VpcId=vpc.id,
)
print(f"Created Subnet: {subnet.id}")

# 3. Create Internet Gateway and attach it
igw = ec2_resource.create_internet_gateway()
vpc.attach_internet_gateway(InternetGatewayId=igw.id)
print(f"Created and attached Internet Gateway: {igw.id}")

# 4. Create Route Table and route to IGW
route_table = vpc.create_route_table()
route_table.create_route(DestinationCidrBlock='0.0.0.0/0', GatewayId=igw.id)
route_table.associate_with_subnet(SubnetId=subnet.id)
print(f"Created and associated Route Table: {route_table.id}")

# 5. Create Security Group
security_group = ec2_resource.create_security_group(
    GroupName='MySecurityGroup',
    Description='Allow SSH',
    VpcId=vpc.id
)
security_group.authorize_ingress(
    IpPermissions=[
        {
            'IpProtocol': 'tcp',
            'FromPort': 22,
            'ToPort': 22,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
        }
    ]
)
print(f"Created Security Group: {security_group.id}")

# 6. Launch EC2 Instance in the Subnet
instances = ec2_resource.create_instances(
    ImageId='ami-12345678',  # LocalStack fake AMI
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='my-key',  # Key pair should exist in LocalStack
    NetworkInterfaces=[{
        'SubnetId': subnet.id,
        'DeviceIndex': 0,
        'AssociatePublicIpAddress': True,
        'Groups': [security_group.id]
    }]
)

instance = instances[0]
instance.wait_until_running()
instance.reload()
print(f"Launched EC2 Instance: {instance.id} in Subnet: {subnet.id}")

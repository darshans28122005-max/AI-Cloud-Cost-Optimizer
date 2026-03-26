import boto3

# Create EC2 client
ec2 = boto3.client('ec2', region_name='us-east-1')

# Get all instances
response = ec2.describe_instances()

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        state = instance['State']['Name']

        print(f"Instance: {instance_id}, State: {state}")

        # Stop running instances
        if state == 'running':
            ec2.stop_instances(InstanceIds=[instance_id])
            print(f"Stopped: {instance_id}")
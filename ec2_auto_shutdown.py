import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instances()

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        state = instance['State']['Name']

        print(f"{instance_id} → {state}")
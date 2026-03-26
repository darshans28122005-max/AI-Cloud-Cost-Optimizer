import boto3

# Create EC2 client
ec2 = boto3.client('ec2', region_name='us-east-1')

def stop_running_instances():
    try:
        response = ec2.describe_instances()

        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                state = instance['State']['Name']

                print(f"Instance ID: {instance_id} | State: {state}")

                if state == 'running':
                    ec2.stop_instances(InstanceIds=[instance_id])
                    print(f"Stopped instance: {instance_id}")

    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    stop_running_instances()
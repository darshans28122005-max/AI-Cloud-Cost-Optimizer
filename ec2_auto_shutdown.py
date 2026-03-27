import boto3
from datetime import datetime, timedelta, timezone

region = 'ap-southeast-2'

ec2 = boto3.client('ec2', region_name=region)
cloudwatch = boto3.client('cloudwatch', region_name=region)
sns = boto3.client('sns', region_name=region)

topic_arn = "PASTE_YOUR_SNS_TOPIC_ARN_HERE"

instances = ec2.describe_instances()

for reservation in instances['Reservations']:
    for instance in reservation['Instances']:

        instance_id = instance['InstanceId']
        print(f"\nChecking Instance: {instance_id}")

        end_time = datetime.now(timezone.utc)
        start_time = end_time - timedelta(minutes=20)

        response = cloudwatch.get_metric_statistics(
            Namespace='AWS/EC2',
            MetricName='CPUUtilization',
            Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
            StartTime=start_time,
            EndTime=end_time,
            Period=300,
            Statistics=['Average']
        )

        datapoints = response['Datapoints']

        if datapoints:
            latest = sorted(datapoints, key=lambda x: x['Timestamp'])[-1]
            cpu = latest['Average']

            print(f"CPU Usage: {cpu:.2f}%")

            with open("log.txt", "a") as f:
                f.write(f"{instance_id} - CPU: {cpu:.2f}%\n")

            if cpu < 5:
                print("Idle → Stopping instance")

                ec2.stop_instances(InstanceIds=[instance_id])

                sns.publish(
                    TopicArn=topic_arn,
                    Message=f"Instance {instance_id} stopped (CPU {cpu:.2f}%)",
                    Subject="EC2 Auto Stop Alert"
                )
            else:
                print("Active")

        else:
            print("No data")
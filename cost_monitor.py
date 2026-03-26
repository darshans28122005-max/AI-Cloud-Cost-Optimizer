import boto3

ce = boto3.client('ce', region_name='us-east-1')

response = ce.get_cost_and_usage(
    TimePeriod={
        'Start': '2024-01-01',
        'End': '2024-12-31'
    },
    Granularity='MONTHLY',
    Metrics=['UnblendedCost']
)

for result in response['ResultsByTime']:
    print("Month:", result['TimePeriod']['Start'])
    print("Cost:", result['Total']['UnblendedCost']['Amount'])
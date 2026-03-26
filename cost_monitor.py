import boto3

# Create Cost Explorer client
ce = boto3.client('ce', region_name='us-east-1')

def get_cost():
    try:
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
            print("-----------------------------")

    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    get_cost()
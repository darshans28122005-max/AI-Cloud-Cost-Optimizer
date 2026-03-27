import boto3
from datetime import date

ce = boto3.client('ce', region_name='us-east-1')

def get_cost():
    try:
        response = ce.get_cost_and_usage(
            TimePeriod={
                'Start': '2024-01-01',
                'End': str(date.today())
            },
            Granularity='MONTHLY',
            Metrics=['UnblendedCost']
        )

        for result in response['ResultsByTime']:
            print("Month:", result['TimePeriod']['Start'])
            print("Cost:", result['Total']['UnblendedCost']['Amount'])
            print("----------------------")

    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    get_cost()
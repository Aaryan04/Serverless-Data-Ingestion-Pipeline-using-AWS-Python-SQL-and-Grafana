import json
import boto3
import urllib3
import datetime

# Replace with your Data Firehose name
FIREHOSE_NAME = 'PUT-S3-y4x8i'

def lambda_handler(event, context):
    
    # Initialize HTTP request manager
    http = urllib3.PoolManager()
    
    # Replace with your Stock API endpoint and API Key
    url = f"https://api.polygon.io/v2/aggs/ticker/NVDA/range/1/day/2023-01-01/2023-12-31?adjusted=true&sort=asc&apiKey=ezOPONq3sVyJPgGrp_wwIt8wk5rxnNnL"
    
    # Make the API request
    r = http.request("GET", url)
    
    # Convert the response into a dictionary
    r_dict = json.loads(r.data.decode(encoding='utf-8', errors='strict'))
    
    # Extract the list of stock data records
    stock_data_list = r_dict.get('results', [])
    
    # Initialize Kinesis Firehose client
    fh = boto3.client('firehose')
    
    # Iterate over the stock data and send each record to Kinesis
    for stock_record in stock_data_list:
        processed_dict = {}
        processed_dict['symbol'] = r_dict.get('ticker', 'NVDA')  # Stock symbol
        processed_dict['date'] = datetime.datetime.utcfromtimestamp(stock_record['t'] / 1000).strftime('%Y-%m-%d %H:%M:%S')  # Convert Unix timestamp to human-readable format
        processed_dict['open'] = stock_record['o']
        processed_dict['close'] = stock_record['c']
        processed_dict['high'] = stock_record['h']
        processed_dict['low'] = stock_record['l']
        processed_dict['volume'] = stock_record['v']
        processed_dict['average_price'] = stock_record['vw']  # Volume-weighted average price
        processed_dict['transactions'] = stock_record['n']  # Number of transactions
        processed_dict['row_ts'] = str(datetime.datetime.now())  # Current timestamp
        
        # Convert the processed dictionary to a JSON string
        msg = json.dumps(processed_dict) + '\n'
        
        # Put record to Kinesis Firehose
        try:
            response = fh.put_record(
                DeliveryStreamName=FIREHOSE_NAME,
                Record={
                    'Data': msg
                }
            )
            print(f"Record sent for date: {processed_dict['date']}")
        except Exception as e:
            print(f"Error sending record for date {processed_dict['date']}: {e}")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Stock data successfully ingested into Kinesis Firehose.')
    }

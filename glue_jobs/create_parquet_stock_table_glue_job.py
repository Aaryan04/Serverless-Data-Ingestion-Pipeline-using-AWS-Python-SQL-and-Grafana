import sys
import boto3

client = boto3.client('athena')

NEW_TABLE_NAME = 'nvda_stocks_data_parquet_table'
NEW_TABLE_S3_BUCKET = 's3://nvda-stock-data-parquet-bucket/'
MY_DATABASE = 'de_project_database'
SOURCE_TABLE_NAME = 'stock_nvda_stocks_data_bucket'
QUERY_RESULTS_S3_BUCKET = 's3://query-results-nvda-stocks-data'

# Refresh the table
queryStart = client.start_query_execution(
    QueryString = f"""
    CREATE TABLE {NEW_TABLE_NAME} 
    WITH (
        external_location='{NEW_TABLE_S3_BUCKET}',
        format='PARQUET',
        write_compression='SNAPPY',
        partitioned_by = ARRAY['yr_mo_partition']
        )           
    AS 

    SELECT
        symbol,
        date,
        open,
        high,
        low,
        close,
        volume,
        average_price,
        DATE_FORMAT(parse_datetime(date, 'yyyy-MM-dd HH:mm:ss'), '%Y-%m') AS yr_mo_partition
    FROM "{MY_DATABASE}"."{SOURCE_TABLE_NAME}"
    ORDER BY 
        date;
    ;
    """,
    QueryExecutionContext = {
        'Database': f'{MY_DATABASE}'
    }, 
    ResultConfiguration = { 'OutputLocation': f'{QUERY_RESULTS_S3_BUCKET}'}
)

# list of responses
resp = ["FAILED", "SUCCEEDED", "CANCELLED"]

# get the response
response = client.get_query_execution(QueryExecutionId=queryStart["QueryExecutionId"])

# wait until query finishes
while response["QueryExecution"]["Status"]["State"] not in resp:
    response = client.get_query_execution(QueryExecutionId=queryStart["QueryExecutionId"])
    
# if it fails, exit and give the Athena error message in the logs
if response["QueryExecution"]["Status"]["State"] == 'FAILED':
    sys.exit(response["QueryExecution"]["Status"]["StateChangeReason"])
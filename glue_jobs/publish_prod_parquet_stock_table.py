import sys
import boto3
from datetime import datetime

# Update with NVDA stock data settings
QUERY_RESULTS_BUCKET = 's3://query-results-nvda-stocks-data/'  # S3 bucket for query results
MY_DATABASE = 'de_project_database'  # Athena database
SOURCE_PARQUET_TABLE_NAME = 'nvda_stocks_data_parquet_table'  # Source table with NVDA stock data
NEW_PROD_PARQUET_TABLE_NAME = 'nvda_stocks_data_parquet_table_prod'  # New PROD table name
NEW_PROD_PARQUET_TABLE_S3_BUCKET = 's3://parquet-nvda-stocks-prod'  # S3 location for new table

# create a string with the current UTC datetime
# convert all special characters to underscores
# this will be used in the table name and in the bucket path in S3 where the table is stored
DATETIME_NOW_INT_STR = str(datetime.now()).replace('-', '_').replace(' ', '_').replace(':', '_').replace('.', '_')

client = boto3.client('athena')

# Refresh the table
queryStart = client.start_query_execution(
    QueryString = f"""
    CREATE TABLE {NEW_PROD_PARQUET_TABLE_NAME}_{DATETIME_NOW_INT_STR} WITH
    (external_location='{NEW_PROD_PARQUET_TABLE_S3_BUCKET}/{DATETIME_NOW_INT_STR}/',
    format='PARQUET',
    write_compression='SNAPPY',
    partitioned_by = ARRAY['yr_mo_partition'])
    AS

    SELECT
        *
    FROM "{MY_DATABASE}"."{SOURCE_PARQUET_TABLE_NAME}"

    ;
    """,
    QueryExecutionContext = {
        'Database': f'{MY_DATABASE}'
    }, 
    ResultConfiguration = { 'OutputLocation': f'{QUERY_RESULTS_BUCKET}'}
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

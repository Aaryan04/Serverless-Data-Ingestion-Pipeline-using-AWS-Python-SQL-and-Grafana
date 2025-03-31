# Serverless Data Ingestion Pipeline using AWS

![AWS Architecture](https://img.shields.io/badge/AWS-Architecture-orange)
![Data Engineering](https://img.shields.io/badge/Data-Engineering-blue)
![Serverless](https://img.shields.io/badge/Serverless-Computing-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

A comprehensive serverless data ingestion and processing pipeline built on AWS cloud services, following modern data engineering principles: automation, efficiency, and distributed computing.

## Project Overview

This project demonstrates the implementation of a complete serverless data pipeline using AWS services. The architecture is designed to automatically collect, process, transform, and visualize data without the need to provision or manage servers.

### Key Data Engineering Principles

- **Automation**: Get the right data to the right people at the right time
- **Efficiency**: Optimize for both speed and cost
- **Distributed Computing**: Leverage cloud-based distributed systems for scalability

### Architecture Diagram

```
┌─────────────┐     ┌────────────┐     ┌──────────────┐     ┌─────────┐
│ External API │────▶│ AWS Lambda │────▶│ Amazon Kinesis│────▶│ S3 Bucket│
└─────────────┘     └────────────┘     └──────────────┘     └─────────┘
                           │                                     │
                           │                                     │
                           ▼                                     ▼
                    ┌──────────────┐                      ┌──────────┐
                    │ EventBridge  │                      │ AWS Glue │
                    │ Schedule     │                      │ Crawler  │
                    └──────────────┘                      └────┬─────┘
                                                               │
                                    ┌────────────┐             │
                                    │ AWS Athena │◀────────────┘
                                    └─────┬──────┘
                                          │
                                          ▼
                                    ┌──────────┐
                                    │ Grafana  │
                                    │ Dashboard│
                                    └──────────┘
```

## Project Components

### AWS Services Used

- **Amazon S3 (Simple Storage Service)**
  - Stores raw and processed data files
  - Supports unlimited file storage with individual files up to 5TB
  - Acts as the central data lake for the pipeline

- **AWS Lambda**
  - Executes Python code without provisioning servers
  - Handles API calls and data transformations
  - Triggers data processing based on events

- **Amazon Kinesis Data Firehose**
  - Provides serverless streaming/batching capabilities
  - Automatically scales with increasing data volumes
  - Delivers data reliably to S3 with built-in retry mechanisms

- **AWS Glue**
  - Creates and manages data catalogs
  - Automatically detects schemas through crawlers
  - Orchestrates ETL workflows and data transformations
  - Supports data quality checks

- **Amazon Athena**
  - Provides serverless SQL query capabilities
  - Allows analysis of data stored in S3
  - Supports complex transformations and analytics
  - Charges based on data scanned ($5 per terabyte)

- **AWS EventBridge/CloudWatch**
  - Schedules and automates Lambda function execution
  - Monitors pipeline performance
  - Stores logs for debugging and audit purposes

- **Grafana**
  - Connects to Athena for data visualization
  - Creates interactive dashboards and reports
  - Supports various chart types for data exploration

### Data Flow Process

1. **Data Ingestion**
   - Lambda functions retrieve data from external APIs
   - Data is processed and formatted as needed
   - Results are sent to Kinesis Data Firehose or directly to S3

2. **Data Storage and Cataloging**
   - S3 buckets store raw and processed data
   - Glue crawlers scan S3 data to create and update data catalogs
   - Data partitioning optimizes query performance

3. **Data Transformation**
   - ETL jobs convert data to optimized formats (e.g., Parquet)
   - Transformations apply business logic and calculations
   - Data quality checks ensure integrity

4. **Data Analysis and Visualization**
   - Athena executes SQL queries against data in S3
   - Results are visualized through Grafana dashboards
   - Interactive reports provide business insights

### Implementation Details

#### Data Sources
- Stock market data (NVIDIA/NVDA historical prices)
- Weather data (via Open-Meteo API)

#### Data Formats
- CSV (initial ingestion)
- Parquet (optimized columnar storage for analytics)

#### Key Technical Implementations
- **Partitioning Strategy**: Data partitioned by year/month/day for query optimization
- **Data Quality Checks**: NULL value detection, duplicate record identification
- **Workflow Orchestration**: Conditional execution paths based on data validation
- **Performance Optimization**: Conversion to Parquet format reduces query costs

#### Advanced Analytics
- Moving averages calculations
- MACD (Moving Average Convergence Divergence)
- Bollinger Bands
- Volatility metrics
- Daily percentage changes

## Getting Started

### Prerequisites
- AWS Account with appropriate permissions
- Basic understanding of AWS services
- Python 3.8+ for Lambda functions

### Setup Instructions

1. **Create S3 Buckets**
   - Create a main bucket for raw data storage
   - Create a separate bucket for Athena query results
   - Create additional bucket for Parquet-formatted data

2. **Configure Lambda Functions**
   - Set up IAM roles with appropriate S3, Kinesis, and Athena permissions
   - Deploy the data ingestion Lambda functions
   - Set timeout to at least 10 seconds for first-time "warm-up"

3. **Set Up Kinesis Firehose**
   - Configure delivery stream to S3
   - Set appropriate buffer size and interval
   - Configure error handling and retry policies

4. **Configure AWS Glue**
   - Create a Glue service role
   - Deploy crawlers to automatically detect schemas
   - Set up ETL jobs for data transformation and quality checks

5. **Create Athena Tables**
   - Set up databases and tables based on the Glue catalog
   - Configure query result location in S3
   - Create views for common analytical queries

6. **Set Up EventBridge Triggers**
   - Create rules to schedule Lambda functions
   - Configure workflow triggers based on data events
   - Set up monitoring for failed executions

7. **Connect Grafana to Athena**
   - Configure Grafana data source
   - Set up appropriate IAM permissions
   - Create visualization dashboards

## Visualization Examples

The project includes several visualization dashboards:

- **Stock Price Trends Over Time (Line Chart)**
  ```sql
  SELECT 
    parse_datetime(date, 'yyyy-MM-dd HH:mm:ss') AS date_parsed,
    close 
  FROM 
    nvda_stocks_data_parquet_table 
  WHERE 
    $__timeFilter(parse_datetime(date, 'yyyy-MM-dd HH:mm:ss'))
  ORDER BY 
    date_parsed ASC;
  ```

- **Trading Volume Analysis (Bar Chart)**
- **Price Volatility Heatmap**
- **Technical Indicators (Moving Averages, MACD, Bollinger Bands)**
- **Daily Percentage Change Analysis**

## Future Enhancements

- Add real-time alerting capabilities
- Implement machine learning predictions
- Expand to multiple data sources
- Add interactive filtering in dashboards
- Implement cost optimization techniques

## Resources and References

- [AWS Documentation](https://docs.aws.amazon.com/)
- [Grafana Documentation](https://grafana.com/docs/)
- [Open-Meteo API Documentation](https://open-meteo.com/en/docs)
- [Polygon.io Stock API Documentation](https://polygon.io/docs/stocks/)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- AWS for providing the serverless infrastructure
- Grafana for the visualization capabilities
- Open-source community for various tools and libraries

---

*This project was developed as a demonstration of modern data engineering practices using serverless architecture.*

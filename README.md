🚀 Serverless Data Ingestion Pipeline using AWS
A complete end-to-end serverless data engineering project that ingests, transforms, orchestrates, and visualizes stock market data using modern AWS cloud services.

📌 Project Overview
This project demonstrates a fully serverless data pipeline architecture built on AWS. The pipeline ingests stock data from an external API, processes it using AWS Lambda, stores it in S3, transforms it using Glue and Athena, orchestrates workflows, and finally visualizes it using Grafana dashboards.

🧱 Architecture Overview
The project is divided into four key modules:

1️⃣ Serverless Data Ingestion
Tools Used: S3, Athena, Lambda, EventBridge

Goal: Ingest stock data from an API and store in S3, enabling serverless querying using Athena.

2️⃣ Scaling and Automation
Tools Used: Kinesis Firehose, Glue Crawler, Athena, Lambda

Goal: Scale the ingestion pipeline with streaming data via Kinesis and automate schema generation using Glue Crawlers.

3️⃣ Orchestrating Workflows
Tools Used: AWS Glue (Jobs & Workflows), CloudWatch, S3 (Parquet)

Goal: Build modular ETL jobs, perform data quality checks, and automate workflow orchestration with robust logging.

4️⃣ Data Visualization
Tools Used: Grafana, Athena

Goal: Connect AWS Athena to Grafana and build interactive dashboards to visualize stock trends and patterns.

⚙️ Technologies Used
AWS S3 – Scalable object storage

AWS Lambda – Serverless compute for data ingestion

Amazon Athena – Serverless SQL querying

Amazon Kinesis Firehose – Real-time streaming data ingestion

AWS Glue (Crawlers + Jobs + Workflows) – ETL and orchestration

AWS EventBridge / CloudWatch – Scheduling and monitoring

Grafana – Data visualization and BI

📊 Visualizations (Grafana)
Some of the Grafana dashboards implemented:

📈 Stock Price Trends (Line chart)

📊 Volume Traded Over Time (Bar chart)

🔥 Daily Price Volatility (Heatmap)

📉 Moving Averages (7-day, 30-day)

📊 Daily % Change in Closing Price

⚖️ MACD Indicator

📎 Bollinger Bands

🔗 Live Dashboard Snapshot

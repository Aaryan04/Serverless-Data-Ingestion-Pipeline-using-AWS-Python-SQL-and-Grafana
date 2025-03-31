# 🚀Serverless Data Ingestion Pipeline using AWS

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

![image](https://github.com/user-attachments/assets/6c1963fb-95e5-4876-ae99-8a79ef7c957e)


---

## 🧱 Architecture Overview

The project is divided into **four key modules**:

### 1️⃣ Serverless Data Ingestion
- **Tools Used**: S3, Athena, Lambda, EventBridge
- **Goal**: Ingest stock data from an API and store in S3, enabling serverless querying using Athena.

### 2️⃣ Scaling and Automation
- **Tools Used**: Kinesis Firehose, Glue Crawler, Athena, Lambda
- **Goal**: Scale the ingestion pipeline with streaming data via Kinesis and automate schema generation using Glue Crawlers.

### 3️⃣ Orchestrating Workflows
- **Tools Used**: AWS Glue (Jobs & Workflows), CloudWatch, S3 (Parquet)
- **Goal**: Build modular ETL jobs, perform data quality checks, and automate workflow orchestration with robust logging.

### 4️⃣ Data Visualization
- **Tools Used**: Grafana, Athena
- **Goal**: Connect AWS Athena to Grafana and build interactive dashboards to visualize stock trends and patterns.

---

## ⚙️ Technologies Used

- **AWS S3** – Scalable object storage
- **AWS Lambda** – Serverless compute for data ingestion
- **Amazon Athena** – Serverless SQL querying
- **Amazon Kinesis Firehose** – Real-time streaming data ingestion
- **AWS Glue (Crawlers + Jobs + Workflows)** – ETL and orchestration
- **AWS EventBridge / CloudWatch** – Scheduling and monitoring
- **Grafana** – Data visualization and BI

---

## 📊 Visualizations (Grafana)

Some of the Grafana dashboards implemented:

- 📈 Stock Price Trends (Line chart)
- 📊 Volume Traded Over Time (Bar chart)
- 🔥 Daily Price Volatility (Heatmap)
- 📉 Moving Averages (7-day, 30-day)
- 📊 Daily % Change in Closing Price
- ⚖️ MACD Indicator
- 📎 Bollinger Bands

🔗 [Live Dashboard Snapshot](https://aaryanshah.grafana.net/dashboard/snapshot/88us2MF4cT0v1frgzmGO4O1FY4Lsbz7i)
![image](https://github.com/user-attachments/assets/01503ab2-ee4b-4dda-95f1-ff3733e813ff)

---

## 📂 Folder Structure

```
.
├── lambda/
│   └── ingest_stock_data.py
├── glue_jobs/
│   ├── delete_parquet_weather_table_s3_athena.py
│   ├── dq_checks_parquet_weather_table.py
│   └── publish_prod_parquet_weather_table.py
├── notebooks/
│   └── sql_queries.sql
├── resources/
│   └── sample_output_screenshots/
├── README.md
```

---

## 🧪 Data Sources

- **Polygon.io Stock API**: Used to extract historical stock data for NVIDIA (NVDA).
- **Open-Meteo API** *(optional alternative)*: Real-time weather data ingestion option.

---

## ✅ Key Features

- 100% **serverless architecture** — no EC2 or managed servers.
- Real-time **streaming data ingestion** via Kinesis.
- **Automated schema detection** and table creation with Glue.
- **ETL orchestration** using Glue workflows and triggers.
- **Cost-effective querying** with Parquet & data partitioning.
- **Beautiful and interactive dashboards** with Grafana.

---

## 📈 Benefits

- 💡 **Efficient & Scalable** – Built for big data ingestion and querying at scale.
- ⏱️ **Automated** – End-to-end automation from ingestion to visualization.
- 📊 **Insightful** – Business-ready dashboards for real-world analytics.

---

## 🔐 IAM & Security

Ensure proper IAM roles and permissions:
- Lambda functions must have access to S3, Kinesis, and Firehose.
- Glue must have full access to Athena and related S3 buckets.
- EventBridge / CloudWatch must be allowed to trigger Lambda functions.
![image](https://github.com/user-attachments/assets/b58adae1-7472-4b00-9125-70fad29a3936)

---

## 🧠 Learnings

- How serverless services can be stitched together to build production-ready pipelines.
- The power of orchestrated ETL jobs and workflow management.
- How to optimize cost with partitioning and Parquet formats.
- Real-world dashboarding for business users and stakeholders.

---

## 💡 Future Enhancements

- Add alerting for data quality checks via SNS.
- Plug-in Airflow or Dagster for advanced orchestration.
- Extend to multi-source data (e.g., multiple stock tickers or weather + financial data).

---


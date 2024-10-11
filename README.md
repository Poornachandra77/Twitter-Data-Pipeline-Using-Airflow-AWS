<img width="730" alt="Screenshot 2024-10-11 at 11 12 44 AM" src="https://github.com/user-attachments/assets/d5e8c680-aeea-4eda-81f1-9710c7cfda56">
# Twitter-Data-Pipeline-Using-Airflow-AWS

Twitter ETL with Apache Airflow

# Overview

This project implements an ETL (Extract, Transform, Load) pipeline using Apache Airflow to extract tweets from a specified Twitter account, transform the data into a structured format, and load it into an AWS S3 bucket. The project is built on an EC2 instance, utilizing the Tweepy library for Twitter API interaction and Pandas for data manipulation.

# Project Structure

twitter_etl.py        # ETL script for extracting tweets

twitter_dag.py        # Airflow DAG definition

requirements.txt       # Python dependencies

# Requirements:-
Python 3.6 or higher
Apache Airflow
Tweepy
Pandas
S3FS (for S3 interactions)

# Installation:-
Clone the repository

# Twitter API Keys:

Update the Twitter API credentials in the twitter_etl.py file:

access_key = "YOUR_ACCESS_KEY"
access_secret = "YOUR_ACCESS_SECRET"
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"

# AWS Credentials:

Ensure your AWS credentials are configured in the environment where Airflow runs, or use AWS IAM roles attached to the EC2 instance.
Running the Project

Start Airflow:

Initialize the Airflow database:

Trigger the DAG:

Locate the twitter_dag in the Airflow UI and trigger it manually or wait for the scheduled run (once a day).

# Code Description
twitter_etl.py
This script handles the Twitter API authentication, extracts tweets from a specified account, and saves them in a CSV format. The main steps include:

Authenticating to the Twitter API using Tweepy.
Fetching the latest 200 tweets from the specified user's timeline.
Structuring the data into a list of dictionaries and converting it into a Pandas DataFrame.
Saving the DataFrame to a CSV file.
twitter_dag.py

This script defines an Airflow DAG that orchestrates the ETL process. Key components include:

Default arguments for the DAG (owner, retries, etc.).
A single task that calls the run_twitter_etl function from twitter_etl.py.
Scheduling the DAG to run daily.

# Notes:-
Ensure that your Twitter API keys have sufficient access to retrieve tweets.
Consider implementing logging for better monitoring and debugging of the ETL process.

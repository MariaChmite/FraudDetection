# Fraud Detection System

This repository contains the Fraud Detection System project created by Maria Chmite, Salim Elghersse, and Meriem Lmoubariki.

## Project Overview

The Fraud Detection System is designed to monitor and detect suspicious financial transactions in real-time. It leverages Apache Kafka for messaging and Apache Spark for stream processing, with integration into a PostgreSQL database for storing suspicious transactions.

## Technologies Used

- Apache Kafka
- Apache Spark
- Python
- PostgreSQL

## Setup and Installation

To set up this project, you will need to have Python, Apache Kafka, Apache Spark, and PostgreSQL installed on your system. Follow the steps below to get started:

1. **Apache Kafka Setup**:
   - Ensure Kafka and Zookeeper are running.
   - Create necessary Kafka topics as documented.

2. **Apache Spark Setup**:
   - Install Spark and ensure it is properly configured with your environment.

3. **Database Setup**:
   - Set up a PostgreSQL database.
   - Create the required tables as per the schema provided.

4. **Python Environment**:
   - Set up a Python virtual environment.
   - Install required dependencies as listed in `requirements.txt`.

## Running the Project

1. Start the Kafka producers to simulate the transaction data feed.
2. Run the Spark streaming application to process the incoming transactions.
3. Monitor the dashboard for any suspicious activities flagged by the system.

## Contributors

- **Maria Chmite**
- **Salim Elghersse**
- **Meriem Lmoubariki**

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

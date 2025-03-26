from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, DoubleType, TimestampType
#from sms_sender import send_sms

# Create Spark session with Kafka support
spark = SparkSession.builder \
    .appName("FraudDetection") \
    .master("local[*]") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1") \
    .config("spark.sql.streaming.checkpointLocation", "/home/mariachmite/spark-checkpoint") \
    .config("spark.hadoop.io.nativeio.enabled", "false") \
    .getOrCreate()

# Define schema for incoming data
schema = StructType() \
    .add("transaction_id", StringType()) \
    .add("name", StringType()) \
    .add("amount", DoubleType()) \
    .add("location", StringType()) \
    .add("timestamp", StringType())

# Read from Kafka topic
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "transactions") \
    .option("startingOffsets", "latest") \
    .load()

# Parse JSON messages from Kafka
json_df = df.selectExpr("CAST(value AS STRING)") \
            .select(from_json(col("value"), schema).alias("data")) \
            .select("data.*")

# Simple fraud rule: transactions over $3000 are suspicious
suspicious_df = json_df.filter(col("amount") > 3000)


# Save suspicious transactions to PostgreSQL and send SMS notifications
def save_and_notify(df, epoch_id):
    # Cast columns appropriately
    df = df.withColumn("transaction_id", col("transaction_id").cast("integer")) \
           .withColumn("amount", col("amount").cast("double")) \
           .withColumn("timestamp", col("timestamp").cast("timestamp"))

    # Write to PostgreSQL
    df.write \
        .format("jdbc") \
        .option("url", "jdbc:postgresql://localhost:5432/postgres") \
        .option("dbtable", "suspicious_transactions") \
        .option("user", "postgres") \
        .option("password", "fraud123") \
        .option("driver", "org.postgresql.Driver") \
        .mode("append") \
        .save()
   
# TODO: Uncomment when upgraded to premium Twilio account
  # Send SMS for high-risk transactions (e.g., amount > $4000)
high_risk_transactions = df.filter(col("amount") > 4000).collect()

for row in high_risk_transactions:
    message = (f"⚠️ Suspicious transaction detected!\n"
               f"ID: {row.transaction_id}, Amount: ${row.amount}, "
               f"Location: {row.location}, Time: {row.timestamp}")
        
    # send_sms(message, "+11234567890")  # Replace with your phone number
    print(f"SMS alert would be sent: {message}")


# Stream processing
query = suspicious_df.writeStream \
    .foreachBatch(save_and_notify) \
    .outputMode("append") \
    .start()

query.awaitTermination()

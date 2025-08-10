# Databricks notebook source
from pyspark.sql.functions import current_timestamp, input_file_name
storage_account_name = "juhodemostorage"

raw_path = f"abfss://raw@{storage_account_name}.dfs.core.windows.net/appointments"
bronze_path = f"abfss://bronze@{storage_account_name}.dfs.core.windows.net/appointments"
schema_location = f"abfss://bronze@{storage_account_name}.dfs.core.windows.net/_schemas/appointments"
checkpoint_location = f"abfss://bronze@{storage_account_name}.dfs.core.windows.net/_checkpoints/appointments"

df = (spark.readStream.format("cloudFiles")
      .option("cloudFiles.format", "csv")
      .option("header", "true")
      .option("cloudFiles.schemaLocation", schema_location)
      .load(raw_path)
      .withColumn("_ingested_at", current_timestamp())
      .withColumn("_source_file", input_file_name())
)

(df.writeStream
  .format("delta")
  .option("checkpointLocation", checkpoint_location) 
  .outputMode("append")
  .trigger(availableNow=True) 
  .start(bronze_path)
)
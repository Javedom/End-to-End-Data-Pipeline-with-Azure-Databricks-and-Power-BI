# Databricks notebook source
# Clean bronze -> silver
from pyspark.sql.functions import col, to_timestamp
bronze_path = "abfss://bronze@juhodemostorage.dfs.core.windows.net/appointments"
silver_path = "abfss://silver@juhodemostorage.dfs.core.windows.net/appointments"

bronze = spark.read.format("delta").load(bronze_path)
silver = (bronze
          .withColumn("scheduled_start", to_timestamp(col("scheduled_start")))
          .withColumn("scheduled_end", to_timestamp(col("scheduled_end")))
          .dropDuplicates(["appointment_id"])
         )
silver.write.mode("overwrite").format("delta").save(silver_path)
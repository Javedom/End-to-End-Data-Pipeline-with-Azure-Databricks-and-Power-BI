# Databricks notebook source
# Build gold marts (dim/fact)
from pyspark.sql.functions import col, datediff, expr
silver_path = "abfss://silver@juhodemostorage.dfs.core.windows.net/appointments"
gold_fact = "abfss://gold@juhodemostorage.dfs.core.windows.net/appointments_fact"

silver = spark.read.format("delta").load(silver_path)
fact = (silver
        .withColumn("duration_min", (col("scheduled_end").cast("long") - col("scheduled_start").cast("long"))/60)
       )
fact.write.mode("overwrite").option("overwriteSchema", "true").saveAsTable("rgluvndemo.gold.appointments_fact")
# Databricks notebook source
# Simple data quality checks
from pyspark.sql.functions import col
gold_fact = "abfss://gold@juhodemostorage.dfs.core.windows.net/appointments_fact"
df = spark.read.format("delta").load(gold_fact)

assert df.filter(col("appointment_id").isNull()).count() == 0, "Null appointment_id"
assert df.filter(~col("status").isin("BOOKED","CANCELLED","NO_SHOW","COMPLETED")).count() == 0, "Invalid status"
print("DQ OK")
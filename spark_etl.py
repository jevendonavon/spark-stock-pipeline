from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, max, min, count, round

# Create Spark session
spark = SparkSession.builder \
    .appName("StockAnalysis") \
    .getOrCreate()

# Suppress verbose logs
spark.sparkContext.setLogLevel("ERROR")

# Read your stock CSV
df = spark.read.csv(
    "/home/jeven/stock_prices.csv",
    header=False,
    inferSchema=True
).toDF("date", "open_price", "high_price", "low_price", 
       "close_price", "volume", "ticker", "daily_return", "ma_7")

print("Schema:")
df.printSchema()

print(f"\nTotal rows: {df.count()}")
print("\nSample data:")
df.show(5)

# Analytics — summary per ticker
# Analytics — summary per ticker
summary = df.groupBy("ticker").agg(
    count("*").alias("total_days"),
    round(avg("close_price"), 2).alias("avg_close"),
    round(max("close_price"), 2).alias("max_close"),
    round(min("close_price"), 2).alias("min_close"),
    round(avg("daily_return"), 4).alias("avg_daily_return")
).orderBy("ticker")

summary.write.mode("overwrite").parquet("output/stock_summary")
print("✅ Saved to output/stock_summary")

print("\nStock Summary:")
summary.show()

spark.stop()

# Save output

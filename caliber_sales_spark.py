"""
Assignment: Calculate total products sold in each caliber using PySpark.

Run:
    spark-submit caliber_sales_spark.py sales.csv
"""

import argparse
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as spark_sum


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", nargs="?", default="sales.csv")
    args = parser.parse_args()

    spark = SparkSession.builder.appName("ProductsSoldByCaliber").getOrCreate()

    try:
        sales_df = (
            spark.read
            .option("header", True)
            .option("inferSchema", True)
            .csv(args.input_file)
        )

        required = {"caliber", "quantity_sold"}
        missing = required - set(sales_df.columns)
        if missing:
            raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")

        result = (
            sales_df
            .filter(col("caliber").isNotNull())
            .groupBy("caliber")
            .agg(spark_sum("quantity_sold").alias("total_products_sold"))
            .orderBy("caliber")
        )

        print("Total number of products sold in each caliber:")
        result.show(truncate=False)

    finally:
        spark.stop()


if __name__ == "__main__":
    main()

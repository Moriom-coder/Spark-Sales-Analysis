# Number of Products Sold in Each Caliber Using Apache Spark

**Name:** Moriom Choudhury  
**Registration Number:** [Enter your registration number]

## Aim
To write a PySpark program to calculate the total number of products sold in each caliber from a sales dataset.

## Tools and Technologies
- Python
- Apache Spark (PySpark)
- CSV dataset

## Dataset
`sales.csv` is an illustrative sample dataset created for this assignment because no original sales dataset was provided. It contains product ID, product name, caliber, and quantity sold. These are sample values, not actual business sales.

## Procedure
1. Create a Spark session.
2. Read the sales CSV file using PySpark.
3. Group records by the `caliber` column.
4. Add the values in `quantity_sold` for each caliber.
5. Display the result.

## How to Run
Install PySpark:

```bash
pip install pyspark
```

Run from this folder:

```bash
spark-submit caliber_sales_spark.py sales.csv
```

## Expected Output
Based on the included sample dataset:

| Caliber | Total products sold |
|---|---:|
| Large | 23 |
| Medium | 32 |
| Small | 32 |

## Conclusion
Thus, the PySpark program groups sales records by caliber and calculates the total quantity of products sold in each caliber.

import pyspark

from delta import *

builder = pyspark.sql.SparkSession.builder.appName("MyApp") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

spark = configure_spark_with_delta_pip(builder).getOrCreate()

df = spark.read.csv("./people.csv", inferSchema=True, header=True)

df.show()

df.write.format("delta").csv("people_delta", inferSchema=True, header="True")

df1 = spark.read.format("delta").csv("/people_delta/part-00000-e96bc6ed-6a2d-4f4e-8292-dd969faa8939-c000.csv",inferSchema=True, header=True)

df1.show()

df1.count()
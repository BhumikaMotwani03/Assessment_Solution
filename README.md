# Setup Instructions:
1. Install the local standalone instance of Apache Spark (3.1.2 version) and extract it into C:\spark
2. Download the hadoop winutils.exe file according to Spark version into C:\spark\bin\.
3. In User variable, add SPARK_HOME with value C:\spark.
4. In System variable, add %SPARK_HOME%\bin to PATH variable.
5. Execute “spark-shell” on cmd to verify spark installation.
6. Install Delta Lake using 'pip install delta-spark' and then configure the SparkSession with the configure_spark_with_delta_pip() utility function in Delta Lake.

## Execution Instructions:
1. Run solution.py file through following command:
     spark-submit solution.py

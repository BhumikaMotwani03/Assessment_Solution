# Setup Instructions:
1. Install the local standalone instance of Apache Spark (3.1.2 version) and extract it into C:\spark
2. Download the hadoop winutils.exe file according to Spark version into C:\spark\bin\.
3. In User variable, add SPARK_HOME with value C:\spark.
4. In System variable, add %SPARK_HOME%\bin to PATH variable.
5. Execute “spark-shell” on cmd to verify spark installation.

# Execution Instructions:
1. Install Delta Lake using 'pip install delta-spark' and then configure the SparkSession with the configure_spark_with_delta_pip() utility function in Delta Lake.
2. Read people.csv into datarame by specifying the path of the file: "/people.csv" with inferSchema and header as true.
3. After that write the above dataframe to local file in delta format by specifying the path of the folder: "people_delta" with inferSchema and header as true.
4. Now, again read the above file into dataframe in delta format by specifying the path of the file: "/people_delta/part-00000-e96bc6ed-6a2d-4f4e-8292-dd969faa8939-c000.csv" inferSchema and header as true.
5. Use count() function to get the record count of above dataframe.

# Refer solution.py file for the PySpark code and people_delta folder containing file which needs to be read in delta format.
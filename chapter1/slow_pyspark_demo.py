import sys
import time
from pyspark.sql import SparkSession
def main():
    # Wait for 3 mins before starting Spark Session
    time.sleep(180)
    spark = SparkSession.builder.appName("pyspark_Demo.py").enableHiveSupport().getOrCreate()
    words = spark.sparkContext.parallelize (["scala","java","hadoop","spark","akka","spark vs hadoop","pyspark","pyspark and spark"])

    counts = words.count()
    print("Number of elements in RDD -> %i" % (counts))

if __name__ == '__main__':
   main()

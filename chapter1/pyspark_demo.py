import sys
from pyspark.sql import SparkSession
def main():

    spark = SparkSession.builder.appName("pyspark_Demo.py").enableHiveSupport().getOrCreate()
    words = spark.sparkContext.parallelize (["scala","java","hadoop","spark","akka","spark vs hadoop","pyspark","pyspark and spark"])

    counts = words.count()
    print "Number of elements in RDD -> %i" % (counts)

if __name__ == '__main__':
   main()

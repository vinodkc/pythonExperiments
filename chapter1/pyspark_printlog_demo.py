import sys
import time
from pyspark.sql import SparkSession

def testFunction(word):
   print("This call is from Python daemon spawned by executor. Processing value -> %s" % (word))
   return (word, 1)

def main():

    print("This call is from Pyspark driver Process, before starting Java driver")
    spark = SparkSession.builder.appName("pyspark_Demo.py").enableHiveSupport().getOrCreate()

    print("This call is from Pyspark driver Process, after starting Java driver")

    words = spark.sparkContext.parallelize (["scala","java","hadoop","spark","akka","spark vs hadoop","pyspark","pyspark and spark"])


    words_map = words.map(testFunction)

    print("This call is from Pyspark driver Process, calling action : count()")
    counts = words_map.count()
    print( "Number of elements in RDD -> %i" % (counts))

if __name__ == '__main__':
   main()

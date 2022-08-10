#!/usr/bin/env python


# eg : http://c120-node3:8088/ws/v1/cluster/apps?state=ACCEPTED 
import sys
import json
from jsonpath_ng.ext import parse
import requests
import time

def main(argv=None):
    if len(sys.argv) < 3:
        print("Usage : CheckYarnApps.py <sleep time> <iterations> <YARN REST URL>" )
        return 0
    
    sleepTime = sys.argv[1]
    iteration = int(sys.argv[2])
    yarnRestUrl = sys.argv[3]
   
    print("This test will iterate " + str(iteration) + " times with a pause of " + sleepTime + " seconds between consecutive REST API calls")
    print("Calling Yarn API " + yarnRestUrl)
    i = 0
    while i < iteration:   
    	appIDs_set1 = callYarnRestAPI(yarnRestUrl)
    	print("Iteration " + str(i)  +" Attempt 1 , Application ID count: " + str(len(appIDs_set1)))
    	time.sleep(int(sleepTime)) 
    	appIDs_set2 = callYarnRestAPI(yarnRestUrl)
    	print("Iteration " + str(i)  +" Attempt 2 , Application ID count: " + str(len(appIDs_set2)))
    	print("Intersection of YARN AppIds in last " + sleepTime + " seconds ")
    	print(appIDs_set1.intersection(appIDs_set2))
        time.sleep(int(sleepTime))
        i += 1
    return 0


def callYarnRestAPI(parameters):
    """Call YARN API and parse JSON"""
    
    responds = requests.get(parameters)
  
    json_data  = responds.json()
    
    jsonpath_expression = parse("apps.app[*].id")
    match = jsonpath_expression.find(json_data)
    
    appIDs = set() 
    for match in jsonpath_expression.find(json_data):
       appIDs.add(match.value)
    return appIDs

if __name__ == '__main__':
    sys.exit(main())


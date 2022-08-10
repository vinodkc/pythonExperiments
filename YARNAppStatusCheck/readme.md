Steps to test
----------------
Step 1) Login to gateway node and install these  python modules 'requests', 'jsonpath-ng'

eg:

pip install requests
pip install jsonpath-ng

Step 2) Run the python script 'CheckYarnApps.py'

eg :

python  CheckYarnApps.py 60 5 "https://abc.com/ws/v1/cluster/apps?state=ACCEPTED"

This test script will print the intersection of two consecutive set of applications in  `ACCEPTED` state 

Expected Sample Output :

```
This test will iterate 5 times with a pause of 60 seconds between consecutive REST API calls
Calling Yarn API <REST URL>
Iteration 0 Attempt 1 , Application ID count: 1
Iteration 0 Attempt 2 , Application ID count: 1
Intersection of YARN AppIds in last 2 seconds
set([application_1635806196684_0011])
Iteration 1 Attempt 1 , Application ID count: 1
Iteration 1 Attempt 2 , Application ID count: 1
Intersection of YARN AppIds in last 2 seconds
set([application_1635806196684_0011])
Iteration 2 Attempt 1 , Application ID count: 0
Iteration 2 Attempt 2 , Application ID count: 0
Intersection of YARN AppIds in last 2 seconds
set([])
Iteration 3 Attempt 1 , Application ID count: 0
Iteration 3 Attempt 2 , Application ID count: 0
Intersection of YARN AppIds in last 2 seconds
set([])
Iteration 4 Attempt 1 , Application ID count: 0
Iteration 4 Attempt 2 , Application ID count: 0
Intersection of YARN AppIds in last 2 seconds
set([])
```

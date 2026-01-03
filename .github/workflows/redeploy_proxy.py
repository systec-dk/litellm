"""

redeploy_proxy.py
"""

import os
import requests
import time

# send a get request to this endpoint
deploy_hook1 = os.getenv("LOAD_TEST_REDEPLOY_URL1")
if not deploy_hook1:
    print("LOAD_TEST_REDEPLOY_URL1 not set, skipping redeploy")
else:
    response = requests.get(deploy_hook1, timeout=20)
    print(f"Sent GET request to deploy_hook1, status: {response.status_code}")


deploy_hook2 = os.getenv("LOAD_TEST_REDEPLOY_URL2")
if not deploy_hook2:
    print("LOAD_TEST_REDEPLOY_URL2 not set, skipping redeploy")
else:
    response = requests.get(deploy_hook2, timeout=20)
    print(f"Sent GET request to deploy_hook2, status: {response.status_code}")

print("SENT GET REQUESTS to re-deploy proxy")
print("sleeeping.... for 60s")
time.sleep(60)

import requests
import sys


url = "http://time-net.online.extra"

print(f"🕵️  SRE Watchdog is checking: {url} ...")

try:
    
    response = requests.get(url, timeout=5)

   
    if response.status_code == 200:
        print("✅ SUCCESS: Website is online and healthy!")
        print(f"   Response Time: {response.elapsed.total_seconds()} seconds")
        sys.exit(0) 
    else:
        print(f"❌ FAILURE: Website returned status code {response.status_code}")
        sys.exit(1) 

except requests.exceptions.RequestException as e:
    
    print(f"❌ CRITICAL FAILURE: Could not connect to site.")
    print(f"   Error: {e}")
    sys.exit(1)
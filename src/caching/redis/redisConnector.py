import redis
import requests
import json

from termcolor import colored


# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Send a ping request and check the response
response = r.ping()

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}


# Function to fetch user data either from the cache or the external route
def fetch_user_data(user_id):
    # Check if data is available in the cache
    user_data = r.get(user_id)


    if user_data is None:
        # Fetch data from the external route
        response = requests.get(f'http://127.0.0.1:5000/api/users/{user_id}', headers=headers, verify=False)


        if response.status_code == 200:
            user_data = response.json()
        else:
            print(f"Error: Received status code {response.status_code}")
            user_data = {}
        # Store the fetched the data in the cache for future requests
        r.set(user_id, json.dumps(user_data))
 
    return user_data


# Function to call service and cache and compare the response
def execute_comparision_code(user_id):
    # Fetch user data using caching
    cached_user_data = fetch_user_data(user_id)
 
    # Fetch user data directly from the external route
    response = requests.get(f'http://127.0.0.1:5000/api/users/{user_id}', headers=headers, verify=False)
    print(response)
    print(response.json())

    if response.status_code == 200:
        external_user_data = response.json()
        print(external_user_data)
        print(cached_user_data)
        print(json.dumps(external_user_data))
    else:
        print(f"Error: Received status code {response.status_code}")
        external_user_data = {"error": "error call"}
    
    # Compare the data
    print(f'{cached_user_data.decode('utf-8')}  {json.dumps(external_user_data)}')
    if cached_user_data == json.dumps(external_user_data):
        print(colored("Data retrieved from cache matches data fetched from the external route.", "green"))
    else:
        print(colored("Data mismatch: Cached data differs from data fetched from the external route.", "red"))
        r.set(user_id, json.dumps(external_user_data))
        print(colored("cache updated with updated response", "yellow"))


for user_id in range(100):
    print(f'Executing for {user_id} ...\n')
    execute_comparision_code(user_id)

for user_id in range(50):
    print(f'Executing for {user_id} ...\n')
    execute_comparision_code(user_id)
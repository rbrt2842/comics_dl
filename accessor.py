import requests
import time

def get_json(url):
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 429:
        retry_after = response.headers.get("Retry-After")
        print(f"Rate limited. Wait {retry_after} seconds before retrying.")
        time.sleep(int(retry_after) if retry_after else 5)
        return get_json(url)
    else:
        print(f"Failed to fetch {url} (status {response.status_code})")
        return None
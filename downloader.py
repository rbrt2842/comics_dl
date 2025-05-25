import os
import re
import requests

def sanitize_filename(name):
    name = name.lower()
    name = re.sub(r'[^\w\s-]', '', name) 
    name = re.sub(r'\s+', '_', name) 
    return name

def download_image(url, filename):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"Downloaded {filename}")
    else:
        print(f"Failed to download image from {url} (status {response.status_code})")

def ensure_output_dir(output_dir):
    output_dir_with_covers = f"{output_dir}_covers"
    os.makedirs(output_dir_with_covers, exist_ok=True)
    return output_dir_with_covers
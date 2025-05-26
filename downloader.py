import os
import re
import requests
import time
import shutil

def sanitize_filename(name):
    name = name.lower()
    name = re.sub(r'[^\w\s-]', '', name) 
    name = re.sub(r'\s+', '_', name) 
    return name

def download_image(url, filename, logger=None, issue_number=None):
    start_time = time.time()
    response = requests.get(url, stream=True)
    
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        message = f"Downloaded {filename}"
        success = True
    elif response.status_code == 429:
        retry_after = response.headers.get("Retry-After", "5")
        message = f"Rate limited. Wait {retry_after} seconds before retrying."
        success = False
        if logger and issue_number:
            logger.log_rate_limit(issue_number, retry_after)
    else:
        message = f"Failed to download image from {url} (status {response.status_code})"
        success = False
    
    duration = time.time() - start_time
    print(message)
    
    if logger and issue_number and response.status_code != 429:
        logger.log_download(issue_number, success, duration)
    
    return success

def ensure_output_dir(output_dir):
    output_dir_with_covers = f"{output_dir}_covers"
    os.makedirs(output_dir_with_covers, exist_ok=True)
    return output_dir_with_covers

def remove_cover_directories(base_path="."):
    for root, dirs, files in os.walk(base_path, topdown=False):
        for dir_name in dirs:
            if dir_name.endswith('_covers'):
                dir_path = os.path.join(root, dir_name)
                try:
                    print(f"Removing directory: {dir_path}")
                    shutil.rmtree(dir_path)
                except Exception as e:
                    print(f"Failed to remove {dir_path}: {e}")
from accessor import get_json
from downloader import sanitize_filename, download_image, ensure_output_dir
from logger import ComicDownloadLogger
import time
import os

def download_series_covers(series_api_url, output_dir="covers"):
    output_dir = ensure_output_dir(output_dir) 
    series_data = get_json(series_api_url)
    if not series_data:
        return

    series_name = sanitize_filename(series_data.get("name", "series"))
    
    logger = ComicDownloadLogger(series_name)
    logger.start_session()
    
    issue_urls = series_data.get("active_issues", [])
    
    for i, issue_url in enumerate(issue_urls, start=1):
        issue_data = get_json(issue_url)
        if not issue_data:
            continue

        cover_url = issue_data.get("cover")
        if not cover_url:
            print(f"No cover found for issue {i}")
            continue

        issue_number = issue_data.get("descriptor", f"{i}")
        filename = os.path.join(output_dir, f"{series_name}_{issue_number.zfill(2)}.jpg")
        
        download_image(cover_url, filename, logger=logger, issue_number=issue_number)
        time.sleep(0.5)
    
    logger.end_session()
    print("Finished downloading covers")
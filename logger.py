import os
import time
from datetime import datetime

class ComicDownloadLogger:
    def __init__(self, series_name):
        self.series_name = series_name
        self.start_time = None
        self.total_images = 0
        self.successful_downloads = 0
        self.failed_downloads = 0
        self.individual_times = []
        
        self.logs_dir = "comic_cover_logs"
        os.makedirs(self.logs_dir, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.log_filename = f"{self.logs_dir}/{self.series_name}_{timestamp}.log"
        
    def start_session(self):
        self.start_time = time.time()
        self._write_to_log(f"Download session started for series: {self.series_name}")
        self._write_to_log(f"Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
    def log_download(self, issue_number, success, duration):
        self.total_images += 1
        if success:
            self.successful_downloads += 1
            status = "SUCCESS"
        else:
            self.failed_downloads += 1
            status = "FAILED"
            
        self.individual_times.append(duration)
        log_entry = (f"Issue {issue_number}: {status} - Download time: {duration:.2f} seconds")
        self._write_to_log(log_entry)
        
    def end_session(self):
        end_time = time.time()
        total_duration = end_time - self.start_time
        avg_time = sum(self.individual_times) / len(self.individual_times) if self.individual_times else 0
        
        self._write_to_log("\nSession Summary:")
        self._write_to_log(f"Total images attempted: {self.total_images}")
        self._write_to_log(f"Successful downloads: {self.successful_downloads}")
        self._write_to_log(f"Failed downloads: {self.failed_downloads}")
        self._write_to_log(f"Average download time: {avg_time:.2f} seconds")
        self._write_to_log(f"Total session duration: {total_duration:.2f} seconds")
        self._write_to_log(f"End time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
    def _write_to_log(self, message):
        with open(self.log_filename, 'a', encoding='utf-8') as log_file:
            log_file.write(f"{message}\n")
import argparse
import zipfile
import os
from driver import download_series_covers
from downloader import remove_cover_directories

def compress_directory(directory_path):
    zip_filename = f"{directory_path}.zip"
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, start=directory_path)
                zipf.write(file_path, arcname)
    print(f"Created compressed archive: {zip_filename}")
    return zip_filename

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download cover images from comics.org series API.")
    parser.add_argument("series_url", help="API URL of the series, e.g. https://www.comics.org/api/series/759/")
    parser.add_argument("--output", "-o", help="Output directory", default="covers")
    parser.add_argument("--clean", action="store_true", help="Remove all _covers directories before downloading")
    parser.add_argument("--compress", "-c", action="store_true", help="Compress the output directory after downloading")
    args = parser.parse_args()

    if args.clean:
        remove_cover_directories()
    
    download_series_covers(args.series_url, args.output)
    
    if args.compress:
        output_dir = f"{args.output}_covers"
        if os.path.exists(output_dir):
            compress_directory(output_dir)
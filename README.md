# Comic Covers Downloader

A Python script to download comic book covers from comics.org

## Requirements
- Python 3
- requests library (install with `pip install -r requirements.txt`)

## Usage

python main.py SERIES_URL [--output OUTPUT_DIR] [--clean] [--compress] 

Arguments:
SERIES_URL : API URL of the series

--output, -o Output directory (default: "covers")

--clean Remove all _covers directories before downloading

--compress, -c Compress the output directory after downloading

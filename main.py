import argparse
from driver import download_series_covers

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download cover images from comics.org series API.")
    parser.add_argument("series_url", help="API URL of the series, e.g. https://www.comics.org/api/series/759/")
    parser.add_argument("--output", "-o", help="Output directory", default="covers")
    args = parser.parse_args()

    download_series_covers(args.series_url, args.output)
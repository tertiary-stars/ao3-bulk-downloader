import argparse
import json
import os
import requests
import re

def load_config():
    with open("config.json") as config_file:
        return json.load(config_file)

def get_session():
    try:
        with open("ao3_session.json") as session_file:
            cookies = json.load(session_file)
            session = requests.Session()
            session.cookies.update(cookies)
            return session
    except FileNotFoundError:
        print("Session not found. Run auth_setup.py first.")
        return None

import re

def download_work(work_url):
    """Download a single work from AO3 and save it with the story name."""
    config = load_config()
    download_path = config["download_path"]
    download_format = config["download_format"].lower()

    session = get_session()
    if not session:
        return

    # Convert the work URL to the download URL
    if "/works/" in work_url:
        work_id = work_url.split("/works/")[1].split("/")[0]
        download_url = f"https://archiveofourown.org/downloads/{work_id}/work.{download_format}"
    else:
        print(f"Invalid work URL: {work_url}")
        return

    # Make the request
    response = session.get(download_url)
    if response.status_code == 200:
        # Extract the file name from Content-Disposition header
        content_disposition = response.headers.get("Content-Disposition", "")
        filename_match = re.search(r'filename="([^"]+)"', content_disposition)
        if filename_match:
            filename = filename_match.group(1)
        else:
            filename = f"work.{download_format}"  # Fallback if no header

        # Sanitize the filename
        filename = re.sub(r'[<>:"/\\|?*]', '_', filename)  # Replace invalid characters

        # Save the file
        filepath = os.path.join(download_path, filename)
        os.makedirs(download_path, exist_ok=True)
        with open(filepath, "wb") as file:
            file.write(response.content)
        print(f"Downloaded: {filepath}")
    else:
        print(f"Failed to download from {download_url}. Status code: {response.status_code}")

def download_from_file(file_path):
    """Download works from a file containing URLs."""
    with open(file_path) as file:
        urls = [line.strip() for line in file]
        for url in urls:
            download_work(url)  # Removed `download_all` argument


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download works from AO3.")
    parser.add_argument("--url", help="Download URL of the work")
    parser.add_argument("--urls", help="File containing multiple download URLs")
    args = parser.parse_args()

    if args.url:
        download_work(args.url)
    elif args.urls:
        download_from_file(args.urls)
    else:
        print("Please specify a download URL or file of URLs.")

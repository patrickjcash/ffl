import requests
import csv
import argparse
from datetime import datetime
import config  # Import the configuration from config.py

def fetch_and_upload_data(year, league_id, headers, cookies, json_data):
    # Rest of the function remains the same

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Upload data to API from CSV file')
    parser.add_argument('--csv', required=True, help='Path to the CSV file containing data')
    parser.add_argument('--year', default=str(datetime.now().year), help='Year for the API endpoint')
    args = parser.parse_args()

    csv_path = args.csv
    year = args.year

    json_data = {'draftStrategy': {'draftList': [], 'excludedPlayerIds': []}}
    with open(csv_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            json_data['draftStrategy']['draftList'].append({
                'auctionValue': int(row['auctionValue']),
                'playerId': int(row['playerId']),
            })

    fetch_and_upload_data(year, config.league_id, config.headers, config.cookies, json_data)
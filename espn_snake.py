import requests
import csv
import argparse
from datetime import datetime
import config  # Import the configuration from config.py

def fetch_and_upload_data(year, league_id, team_id, headers, cookies, json_data):
    api_url = f"https://lm-api-writes.fantasy.espn.com/apis/v3/games/ffl/seasons/{year}/segments/0/leagues/{league_id}/teams/{team_id}"
    
    response = requests.post(api_url, json=json_data, headers=headers, cookies=cookies)
    
    if response.status_code == 200:
        print("Data uploaded successfully.")
    else:
        print(f"Error uploading data. Status code: {response.status_code}")
        print("Response content:")
        print(response.content)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Upload data to API from CSV file')
    parser.add_argument('--csv', required=True, help='Path to the CSV file containing data')
    parser.add_argument('--year', default=str(datetime.now().year), help='Year for the API endpoint')
    parser.add_argument('--league_id', default=config.league_id, help='League ID for the API endpoint (default from config)')
    parser.add_argument('--team_id', default=config.team_id, help='Team ID for the API endpoint (default from config)')
    args = parser.parse_args()

    csv_path = args.csv
    year = args.year
    league_id = args.league_id
    team_id = args.team_id

    json_data = {
        'draftStrategy': {
            'draftList': [],
            'excludedPlayerIds': []
        }
    }
    with open(csv_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            json_data['draftStrategy']['draftList'].append({
                'playerId': int(row['playerId']),
            })

    fetch_and_upload_data(year, league_id, team_id, config.headers, config.cookies, json_data)

import requests
import csv
from datetime import datetime

# Placeholders for cookies, headers, and params
cookies = {
    'cookie_name': 'cookie_value'
    # Add other cookies if needed
}

headers = {
    'user-agent': 'Your User Agent',
    'authorization': 'Bearer Your_Auth_Token'
    # Add other headers if needed
}

params = {
    'param_name': 'param_value'
    # Add other parameters if needed
}

def position_id_to_string(position_id):
    position_lookup = {
        1: 'QB',
        2: 'RB',
        3: 'WR',
        4: 'TE',
        5: 'K',
        16: 'DST'
    }
    return position_lookup.get(position_id, 'UNKNOWN')

def update_headers(headers, x_fantasy_filter):
    # Update the 'x-fantasy-filter' header
    headers['x-fantasy-filter'] = x_fantasy_filter
    
    return headers

def fetch_and_export_data(year, league_id, headers, cookies, params):
    # Define the API endpoint URL
    api_url = f'http://fantasy.espn.com/apis/v3/games/ffl/seasons/{year}/segments/0/leagues/{league_id}?view=kona_player_info'

    # Make the API request
    response = requests.get(api_url, headers=headers, cookies=cookies, params=params)
    data = response.json()

    # Extract player data
    players = data['players']

    # Create a CSV file with the current date in the filename
    current_date = datetime.now().strftime('%Y-%m-%d')
    filename = f'{current_date}_{year}_{league_id}.csv'

    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['PLAYER', 'TEAM', 'POS', 'STATUS', 'PTS'])

        for player in players:
            player_data = player['player']
            player_name = player_data['fullName']
            team = player_data['proTeamId']
            position_id = player_data['defaultPositionId']
            injury_status = player_data.get('injuryStatus', '')  # Handle missing 'injuryStatus'
            applied_total = player_data['stats'][0]['appliedTotal']  # Rename stats to applied_total

            position = position_id_to_string(position_id)
            
            csv_writer.writerow([player_name, team, position, injury_status, applied_total])

    print(f'Data exported to {filename}')

if __name__ == '__main__':
    default_year = '2023'
    year = input(f'Enter the year (default: {default_year}): ') or default_year

    default_league_id = '1722379'
    league_id = input(f'Enter the league ID (default: {default_league_id}): ') or default_league_id

    # Prompt for the number of players (limit)
    default_limit = '400'
    limit = input(f'Enter the number of players (default: {default_limit}): ') or default_limit

    # Construct the 'x-fantasy-filter' value
    x_fantasy_filter = (
        '{"players":{"filterSlotIds":{"value":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,24]},'
        f'"filterStatsForExternalIds":{{"value":[{year}]}},'
        '"filterStatsForSourceIds":{"value":[1]},'
        '"sortAppliedStatTotal":{"sortAsc":false,"sortPriority":1,"value":"102023"},'  # Sort in descending order of projected total fantasy points
        '"sortDraftRanks":{"sortPriority":2,"sortAsc":true,"value":"PPR"},'
        '"sortPercOwned":{"sortPriority":4,"sortAsc":false},'
        f'"limit":{limit},'  # Allow fetching more than 50 players
        '"offset":0,'
        '"filterRanksForScoringPeriodIds":{"value":[1]},'
        '"filterRanksForRankTypes":{"value":["PPR"]},'
        '"filterRanksForSlotIds":{"value":[0,2,4,6,17,16]},'
        '"filterStatsForTopScoringPeriodIds":{"value":2,"additionalValue":["002023","102023","002022","022023"]}}}')

    # Update the headers with the x-fantasy-filter
    updated_headers = update_headers(headers.copy(), x_fantasy_filter)

    fetch_and_export_data(year, league_id, updated_headers, cookies, params)

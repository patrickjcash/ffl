import requests
import csv
from datetime import datetime
import config  # Import the configuration from config.py

# Define team_id_to_abbreviation mapping here
team_id_to_abbreviation = {
    1: 'ATL',
    2: 'BUF',
    3: 'CHI',
    4: 'CIN',
    5: 'CLE',
    6: 'DAL',
    7: 'DEN',
    8: 'DET',
    9: 'GB',
    10: 'TEN',
    11: 'IND',
    12: 'KC',
    13: 'LV',
    14: 'LAR',
    15: 'MIA',
    16: 'MIN',
    17: 'NE',
    18: 'NO',
    19: 'NYG',
    20: 'NYJ',
    21: 'PHI',
    22: 'ARI',
    23: 'PIT',
    24: 'LAC',
    25: 'SF',
    26: 'SEA',
    27: 'TB',
    28: 'WAS',
    29: 'CAR',
    30: 'JAC',
    33: 'BAL',
    34: 'HOU'
}

# Define position_id_to_string mapping here
position_id_to_string = {
    1: 'QB',
    2: 'RB',
    3: 'WR',
    4: 'TE',
    5: 'K',
    16: 'DST'
}

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
        csv_writer.writerow(['ID', 'PLAYER', 'TEAM', 'POS', 'STATUS', 'PTS'])

        for player in players:
            player_data = player['player']
            player_id = player['id']
            player_name = player_data['fullName']
            team_id = player_data['proTeamId']
            position_id = player_data['defaultPositionId']
            injury_status = player_data.get('injuryStatus', '')  # Handle missing 'injuryStatus'
            applied_total = player_data['stats'][0]['appliedTotal']  # Rename stats to applied_total

            team = team_id_to_abbreviation.get(team_id, 'UNKNOWN')
            position = position_id_to_string.get(position_id, 'UNKNOWN')

            csv_writer.writerow([player_id, player_name, team, position, injury_status, applied_total])

    print(f'Data exported to {filename}')

if __name__ == '__main__':
    default_year = str(datetime.now().year)
    year = input(f'Enter the year (default: {default_year}): ') or default_year

    league_id = input(f'Enter the league ID (default: {config.league_id}): ') or config.league_id

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
    updated_headers = update_headers(config.headers.copy(), x_fantasy_filter)

    fetch_and_export_data(year, league_id, updated_headers, config.cookies, config.params)

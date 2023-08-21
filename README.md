# ESPN Fantasy Football data scraper and auction draft value uploader

Python script to automate data extraction and upload for ESPN Fantasy Football.

- **espn_scrape.py** pulls projected fantasy point data (based league-specific scoring)
- **espn_update.py** uploads auction draft values

# Requirements

1. Python
2. ESPN account

# Configuration

Find League ID

1. Log in to ESPN Fantasy Football and go to your league
2. From your league homepage, find your League ID in the URL: https://fantasy.espn.com/football/team?leagueId=[LEAGUE_ID]
3. Copy the League ID to **config.py**

While logged in, get API request metadata (cookies, headers, params). You will need to redo these steps occasionally as your cookies/session expiers.

1. Go to https://fantasy.espn.com/football/players/projections
2. Select your league is selected under the "Scoring Type" dropdown
3. Open Chrome Developer Tools --> Network
4. Refresh the page
5. Find the API request that matches this format [LEAGUE_ID]?view=kona_player_info
6. Copy the request by right clicking the request --> Copy --> Copy as cURL
7. Go to https://curlconverter.com/python/ and paste the request
8. Copy the reformatted data blocks for cookies, headers, params and replace the placeholders in **config.py**

# Data scrape

Open Terminal and run 

```
python espn_scrape.py
```

The fantasy data will be retrieved and written to a CSV file.

# Data upload

Open Terminal and run python

```
python espn_update.py --csv data.csv --year 2023 --league_id 987654
```

Year will default to current calendar year. League id will default to config.py value

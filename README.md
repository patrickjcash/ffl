# ESPN Fantasy Football data scraper and auction draft value uploader

Python script to automate data extraction and upload for ESPN Fantasy Football.

- **espn_scrape.py** pulls projected player fantasy scoring data (based on league-specific scoring)
- **espn_update.py** uploads salary cap draft strategy data
- **espn_update.py** uploads snake order draft strategy data

# Requirements

1. Python
2. ESPN account

# Configuration

Find League ID and Team ID

1. Log in to ESPN Fantasy Football and go to My Team page
2. Your Leage ID and Team ID will be in the URL: https://fantasy.espn.com/football/team?leagueId=[LEAGUE_ID]&teamId=[TEAM_ID]
3. Copy the League ID and Team ID to **config.py**

While logged in, get API request metadata (cookies, headers, params). You will need to redo these steps occasionally as your cookies/session expiers.

1. Go to https://fantasy.espn.com/football/players/projections
2. Select your league is selected under the "Scoring Type" dropdown
3. Open Chrome Developer Tools --> Network
4. Refresh the page
5. Find the API request that matches this format [LEAGUE_ID]?view=kona_player_info
6. Copy the request by right clicking the request --> Copy --> Copy as cURL
7. Go to https://curlconverter.com/python/ and paste the request
8. Copy the reformatted data blocks for cookies, headers, params and replace the placeholders in **config.py**

_Note to self: may only need a couple values, depending on Public/Private league settings: https://github.com/joeyagreco/leeger/blob/main/doc/league_loader/espn.md_

# Data scrape

Open Terminal and run:

```
python espn_scrape.py
```

The fantasy data will be retrieved and written to a CSV file.

# Data upload - Salary Cap Draft

Create a CSV with the following values: playerId, auctionValue.

Open Terminal and run:

```
python espn_update.py --csv auction_values.csv --year 2023 --league_id 987654 --team_id 10
```

# Data upload - Snake Draft

Create a CSV with the following value, in order of preference: playerId.

Open Terminal and run:

```
python espn_snake.py --csv snake_order.csv --year 2023 --league_id 987654 --team_id 10
```

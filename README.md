# ESPN Fantasy Football data scraper

Python script to automate collection of league-specific fantasy football player data provided by ESPN.

# Requirements

1. Python
2. ESPN account

# Prepare the script

Find League ID

1. Log in to ESPN Fantasy Football and go to your league
2. From your league homepage, find your League ID in the URL: https://fantasy.espn.com/football/team?leagueId=[LEAGUE_ID]

While logged in, get API request metadata (cookies, headers, params). You will need to redo these steps occasionally as your cookies/session expiers.

1. Go to https://fantasy.espn.com/football/players/projections
2. Select your league is selected under the "Scoring Type" dropdown
3. Open Chrome Developer Tools --> Network
4. Refresh the page
5. Find the API request that matches this format [LEAGUE_ID]?view=kona_player_info
6. Copy the request by right clicking the request --> Copy --> Copy as cURL
7. Go to https://curlconverter.com/python/ and paste the request
8. Copy the reformatted data blocks for cookies, headers, params and replace the placeholders in espn_scrape.py

# Data collection

Open Terminal and run python espn_scrape.py. The fantasy data will be retrieved and written to a CSV file.

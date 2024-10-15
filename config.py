# config.py

# See README for instructions

# League and Team ID (available from ESPN FF URL parameters)

league_id = 'YOUR_LEAGE_ID_HERE'
team_id = 'YOUR_TEAM_ID_HERE'

# Paste SWID and s2 below

SWID = 'YOUR_SWID_HERE'
espn_s2 = 'YOUR_S2_HERE'

cookies = {
    'SWID': '{' + SWID + '}',
    'espn_s2': espn_s2
}

# May need to update - copy/paste from a request

headers = {
    'authority': 'lm-api-reads.fantasy.espn.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,fr;q=0.8',
    # 'cookie': 
    'dnt': '1',
    'if-none-match': 'W/"054bc6b62ff32845a382de9186633e003"',
    'origin': 'https://fantasy.espn.com',
    'referer': 'https://fantasy.espn.com/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'x-fantasy-filter': '{"players":{"filterStatsForExternalIds":{"value":[2022,2023]},"filterSlotIds":{"value":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,24]},"filterStatsForSourceIds":{"value":[0,1]},"useFullProjectionTable":{"value":true},"sortAppliedStatTotal":{"sortAsc":false,"sortPriority":3,"value":"102023"},"sortDraftRanks":{"sortPriority":2,"sortAsc":true,"value":"PPR"},"sortPercOwned":{"sortPriority":4,"sortAsc":false},"limit":50,"filterRanksForSlotIds":{"value":[0,2,4,6,17,16]},"filterStatsForTopScoringPeriodIds":{"value":2,"additionalValue":["002023","102023","002022","022023"]}}}',
    'x-fantasy-platform': 'kona-PROD-5f08dfd3dbb5e6c73d92e732291bff190cfa712d',
    'x-fantasy-source': 'kona',
}

params = {
    'view': 'kona_player_info',
}
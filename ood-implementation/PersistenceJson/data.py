import json 

data = {
  "match_id": "987654321",
  "date": "2024-02-15",
  "time": "20:30:00",
  "venue": "Sports Center",
  "teams": {
    "home_team": {
      "name": "Blue Lightning",
      "score": 105
    },
    "away_team": {
      "name": "Red Raptors",
      "score": 98
    }
  },
  "game_stats": {
    "total_quarters": 4,
    "quarter_scores": [28, 20, 25, 32],
    "player_stats": [
      {
        "player_id": "player001",
        "name": "Chris Johnson",
        "team": "Blue Lightning",
        "points": 30,
        "assists": 8,
        "rebounds": 12
      },
      {
        "player_id": "player002",
        "name": "Sarah Miller",
        "team": "Red Raptors",
        "points": 22,
        "assists": 5,
        "rebounds": 10
      }
    ]
  },
  "winner": "Blue Lightning",
  "mvp": {
    "player_id": "player001",
    "name": "Chris Johnson",
    "team": "Blue Lightning"
  }
}

def load_json():
  # Writing to JSON file
  with open("data.json", "w") as json_data_file:
      json.dump(data, json_data_file)

  # Reading from JSON file
  with open("data.json", "r") as json_data_file:
      loaded_data = json.load(json_data_file)

  print(loaded_data)    
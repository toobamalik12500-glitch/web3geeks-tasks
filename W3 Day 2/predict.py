# Task 5 - Load Saved Models

import joblib

match_winner_model = joblib.load("match_winner_model.pkl")
top_player_model = joblib.load("top_player_model.pkl")

print("Models loaded successfully")

# Task 5 - Match Winner Prediction

import pandas as pd

def predict_match_winner(team_name, opponent, venue, win_streak, last_5_avg_score, head_to_head_wins):
    
    data = pd.DataFrame({
        "team_name": [team_name],
        "opponent": [opponent],
        "venue": [venue],
        "win_streak": [win_streak],
        "last_5_avg_score": [last_5_avg_score],
        "head_to_head_wins": [head_to_head_wins]
    })
    
    prediction = match_winner_model.predict(data)
    
    return prediction[0]
# Test Match Winner Prediction

prediction = predict_match_winner(
    "adelaide crows",
    "hawthorn hawks",
    "Adelaide Oval",
    2,
    85,
    10
)

print("Predicted Match Winner:", prediction)
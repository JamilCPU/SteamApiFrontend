from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from config import Config

load_dotenv()

# Create Flask app
app = Flask(__name__)

STEAM_API_BASE = "https://api.steampowered.com"

STEAM_API_KEY = os.getenv('STEAM_API_KEY')

@app.route('/')
def home():
    """Home endpoint - welcome message"""
    return jsonify({
        "message": "Welcome to Steam API Wrapper",
        "note": "Make sure to set your Steam API key in config.py",
        "endpoints": {
            "get_user_info": "/user/<steam_id>",
            "get_user_games": "/user/<steam_id>/games",
            "get_game_details": "/game/<app_id>",
            "search_games": "/search/games?q=<query>"
        }
    })

if __name__ == '__main__':
    app.run(debug=Config.DEBUG, port=Config.PORT)

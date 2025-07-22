from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from config import Config
import requests

load_dotenv()

# Create Flask app
app = Flask(__name__)

STEAM_API_BASE = "https://api.steampowered.com"

STEAM_API_KEY = os.getenv('STEAM_API_KEY')

@app.route('/')
def home():
    return "Welcome to Steam API Wrapper"

@app.route('/getAppNews')
def getNewsForApp():
    appId = request.args.get('appId')
    count = request.args.get('count')
    maxLength = request.args.get('maxLength')
    format = request.args.get('format')
    params = {
        'appId': appId,
        'count': count,
        'maxLength': maxLength,
        'format': format
    }

    if not appId:
        return jsonify({'400 Bad Request': 'App ID is required'}), 400

    url = f"{STEAM_API_BASE}/ISteamNews/GetNewsForApp/v0002/"

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({'An Internal Server Error has occurred': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=Config.DEBUG, port=Config.PORT)

# config.py
import os


class Config:
    # Set STEAM_API_KEY in the environment; it is never committed.
    STEAM_API_KEY = os.environ.get("STEAM_API_KEY", "")
    
    STEAM_API_BASE = "https://api.steampowered.com"
    
    DEBUG = True
    PORT = 5000
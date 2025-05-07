
"""
like_tweet.py

This script uses the Twitter API v2 to like a tweet via POST request.
It uses Bearer Token authentication and requires a valid tweet ID and user ID.

Environment variables used:
- BEARER_TOKEN: Your Twitter API Bearer Token
- USER_ID: Your Twitter User ID (numeric)
"""

import os
import requests
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

BEARER_TOKEN = os.getenv("BEARER_TOKEN")
USER_ID = os.getenv("USER_ID")  # Your own Twitter user ID

def like_tweet(tweet_id):
    url = f"https://api.twitter.com/2/users/{USER_ID}/likes"
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "tweet_id": tweet_id
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        print(f"✅ Tweet {tweet_id} liked successfully.")
        return True
    elif response.status_code == 403:
        print(f"❌ Forbidden: {response.status_code} - {response.json()}")
        return 403
    elif response.status_code == 401:
        print("❌ Unauthorized - check Bearer Token.")
        return 401
    elif response.status_code == 429:
        print("❌ Rate limit exceeded.")
        return "rate_limit"
    else:
        print(f"❌ Error: {response.status_code} - {response.json()}")
        return None

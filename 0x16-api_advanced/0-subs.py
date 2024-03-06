#!/usr/bin/python3
"""
This module contains a function that queries the reddit API
and returns the number of total subscribers
"""


import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "My-User-Agent"}  # Custom User-Agent header
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get("data")
            if data:
                return data.get("subscribers", 0)
        else:
            return 0
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0

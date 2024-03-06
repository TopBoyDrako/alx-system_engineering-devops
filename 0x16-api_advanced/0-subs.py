#!/usr/bin/python3
"""
This module contains a function that queries the reddit API
and returns the number of total subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    This function queries the reddit api to get the total amount of subcribers
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "My-User-Agent"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code >= 300:
            return 0
        else:
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
    except Exception as e:
        print(f"Error: {e}")
        return 0

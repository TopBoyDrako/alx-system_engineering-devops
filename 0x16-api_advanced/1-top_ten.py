#!/usr/bin/python3
"""
This  is a module for task 1
"""

import requests

def top_ten(subreddit):
    """
    This function queries the Reddit API to print the titles of the first 10 hot posts
    for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "My-User-Agent"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code >= 300:
            print("None")
            return
        else:
            data = response.json()
            for post in data.get("data", {}).get("children", []):
                print(post.get("data", {}).get("title"))
    except Exception as e:
        print(f"Error: {e}")
        print("None")

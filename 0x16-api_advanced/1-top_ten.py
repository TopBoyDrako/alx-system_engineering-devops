#!/usr/bin/python3
"""
This  is a module for task 1
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and returns the top 10 hot posts of the subreddit.
    If the subreddit is invalid, returns None.
    """
    sub_info = requests.get(f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10",
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code >= 300:
        return None
    else:
        return [child.get("data").get("title") for child in sub_info.json().get("data").get("children")]

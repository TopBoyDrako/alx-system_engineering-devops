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

    info = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if info.status_code >= 300:
        return 0

    return info.json().get("data").get("subscribers")

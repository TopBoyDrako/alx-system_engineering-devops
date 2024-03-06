#!/usr/bin/python3
"""
This module contains a function that queries the reddit API
and returns the number of total subscribers
"""
import requests
import json
import sys


def number_of_subscribers(subreddit):
    """
    This function queries the reddit api to get the total amount of subcribers
    """
    username = 'ledbag123'
    password = 'Reddit72'
    user_pass_dict = {'user': username, 'passwd': password, 'api_type': 'json'}
    headers = {'user-agent': '/u/ledbag123 API Python for Holberton School'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    client = requests.session()
    client.headers = headers
    r = client.get(url, allow_redirects=False)
    if r.status_code == 200:
        return (r.json()["data"]["subscribers"])
    else:
        return(0)

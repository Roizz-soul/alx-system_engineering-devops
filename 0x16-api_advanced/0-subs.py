#!/usr/bin/python3
"""Function to query the Reddit API and returns the number of
   subscribers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, allow_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json()
    return (data["data"]["subscribers"])

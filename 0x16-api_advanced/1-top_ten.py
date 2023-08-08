#!/usr/bin/python3
"""Function to query the Reddit API and returns the top ten hot posts
for a given subreddit"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    params = {
        "limit": 10
    }
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        print("None")
        return 0
    data = response.json()
    for i in data["data"]["children"]:
        print(i["data"]["title"])

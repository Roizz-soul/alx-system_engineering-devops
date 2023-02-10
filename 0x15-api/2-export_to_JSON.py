#!/usr/bin/python3
"""Requests info from an api and displays the processed content"""
import csv
import json
import requests
import sys

if __name__ == "__main__":
    uid = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    user_s = requests.get(url + 'users/{}'.format(uid))
    todo_s = requests.get(url + 'todos?userId={}'.format(uid))

    with open('{}.json'.format(uid), 'w') as f:
        json.dump({uid: [{
                "task": data["title"],
                "completed": data["completed"],
                "username": user_s.json()["username"]
                } for data in todo_s.json()]}, f)

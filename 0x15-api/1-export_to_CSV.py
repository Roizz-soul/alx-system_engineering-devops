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

    with open('{}.csv'.format(uid), 'w', newline="") as csvf:
        writer = csv.writer(csvf, quoting=csv.QUOTE_ALL)
        for data in todo_s.json():
            row = ['{}'.format(uid),
                   '{}'.format(user_s.json()["name"]),
                   '{}'.format(data["completed"]),
                   '{}'.format(data["title"])]
            writer.writerow(row)

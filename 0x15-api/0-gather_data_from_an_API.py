#!/usr/bin/python3
"""Requests info from an api and displays the processed content"""
import json
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user_s = requests.get(url + 'users/{}'.format(sys.argv[1]))
    todo_s = requests.get(url + 'todos?userId={}'.format(sys.argv[1]))

    i = 0
    j = 0
    for data in todo_s.json():
        j = j + 1
        if data['completed'] is True:
            i = i + 1

    print('Employee {} is done with tasks({}/{}):'.format(
                user_s.json()['name'], i, j))
    for data in todo_s.json():
        if data['completed'] is True:
            print('\t{}'.format(data['title']))

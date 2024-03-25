#!/usr/bin/python3
"""Extending Python script, in task #0, to export data in the CSV format"""

import csv
import requests
from sys import argv

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    todo = requests.get(url + "todos", params={"userId": argv[1]}).json()
    tasks = []
    for task in todo:
        if task.get('completed') is True:
            tasks.append(task.get('title'))

    with open(str(argv[1]) + ".csv", "w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todo:
            writer.writerow([int(argv[1]), user.get('username'),
                             task.get('completed'), task.get('title')])

#!/usr/bin/python3
"""Extending Python script, in task #0, to export data in the JSON format"""

import json
import requests
from sys import argv

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    todo = requests.get(url + "todos", params={"userId": argv[1]}).json()
    tasks = []
    for task in todo:
        task_dict = {}
        task_dict["task"] = task.get("title")
        task_dict["completed"] = task.get("completed")
        task_dict["username"] = user.get("username")
        tasks.append(task_dict)
    json_obt = {}
    json_obt[argv[1]] = tasks
    with open(argv[1] + ".json", "w") as json_file:
        json.dump(json_obt, json_file)

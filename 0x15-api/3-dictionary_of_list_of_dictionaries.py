#!/usr/bin/python3
"""Extending Python script, in task #0,
   to export data in the JSON format"""

import json
import requests

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"

    user_dict = {}
    name_dict = {}
    users = requests.get(url + "users").json()
    for user in users:
        user_id = user.get("id")
        user_dict[user_id] = []
        name_dict[user_id] = user.get("username")

    todo = requests.get(url + "todos").json()
    for task in todo:
        user_id = task.get("userId")
        task_dict = {}
        task_dict["task"] = task.get("title")
        task_dict["completed"] = task.get("completed")
        task_dict["username"] = name_dict.get(user_id)
        user_dict.get(user_id).append(task_dict)

    with open("todo_all_employees.json", "w") as file:
        json.dump(user_dict, file)

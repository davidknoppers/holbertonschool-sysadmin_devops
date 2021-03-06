#!/usr/bin/python3
"""
Requests username and tasks from JSON Placeholder
based on userid (which is sys.argv[1])
"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    if len(sys.argv) > 1:
        user_id = sys.argv[1]
        name = requests.get("{}/users/{}".format(
            url, user_id)).json().get("name")
        r = requests.get("{}/todos?userId={}".format(
            url, user_id)).json()
        tasks_completed = []
        for task in r:
            if task.get("completed") is True:
                tasks_completed.append(task)
        print("Employee {} is done with tasks({:d}/{:d}):".format(
            name, len(tasks_completed), len(r)))
        if len(tasks_completed) > 0:
            for task in tasks_completed:
                print("\t {}".format(task.get("title")))

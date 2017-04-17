#!/usr/bin/python3
"""
Requests username and tasks from JSON Placeholder
based on userid (which is sys.argv[1])
and saves it to JSON
"""
import sys
import requests
import json


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    if sys.argv[1] and int(sys.argv[1]):
        user_id = sys.argv[1]
        name = requests.get("{}/{}".format(
            url, user_id)).json().get("username")
        r = requests.get("{}/{}/todos".format(
            url, user_id)).json()
        with open("{}.json".format(user_id), mode="w", newline="") as f:
            result = []
            for task in r:
                result.append({"username": name,
                               "completed": task.get("completed"),
                               "task": task.get("title")})
            json.dump({user_id: result}, f)

#!/usr/bin/python3
"""
Requests data from JSON Placeholder
and saves it to JSON as a dictionary of dictionaries
"""
import requests
import json


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    all_users = requests.get(url).json()
    result = {}
    for user in all_users:
        result[user.get("id")] = []
        for task in requests.get("{}/{}/todos".format(
                url, user.get("id"))).json():
            result[user.get("id")].append({"task": task.get("title"),
                                           "completed": task.get("completed"),
                                           "username": user.get("username")})
    with open("todo_all_employees.json", mode="w", newline="") as f:
        json.dump(result, f)

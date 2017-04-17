#!/usr/bin/python3
"""
Requests username and tasks from JSON Placeholder
based on userid (which is sys.argv[1])
and writes it to a csv
"""
import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    if len(sys.argv) > 1:
        user_id = sys.argv[1]
        name = requests.get("{}/{}".format(
            url, user_id)).json().get("username")
        r = requests.get("{}/{}/todos".format(
            url, user_id)).json()
        with open("{}.csv".format(user_id), mode="w") as f:
            result = csv.writer(f, delimiter=",",
                                quotechar='"', quoting=csv.QUOTE_ALL)
            for task in r:
                temp = [user_id, name, task.get("completed"),
                        task.get("title")]
                result.writerow(temp)

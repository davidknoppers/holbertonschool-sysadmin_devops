#!/usr/bin/python3
"""
Queries the Reddit API
And gets the top ten hot posts for a subreddit, if possible
We loop through the deep dictionary returned as a JSON and print the titles
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API
    And gets the top ten hot posts for a subreddit, if possible
    We loop through the deep dictionary returned as a JSON and print the titles
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    r = requests.get(url, headers={'user-agent': 'Chrome'})
    top_list = []
    counter = 0
    try:
        for child in r.json()['data'].get('children'):
            top_list.append(child['data'].get('title'))
            counter += 1
            if counter > 9:
                break
        print("\n".join(top for top in top_list))
    except Exception as err:
        print("None")

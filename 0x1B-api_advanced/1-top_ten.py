#!/usr/bin/python3
"""
Queries the Reddit API
And gets the top ten hot posts for a subreddit, if possible
We loop through the deep dictionary returned as a JSON and print the titles
"""

import requests


def top_ten(subreddit=None):
    """
    Queries the Reddit API
    And gets the top ten hot posts for a subreddit, if possible
    We loop through the deep dictionary returned as a JSON and print the titles
    """
    if subreddit is None:
        return None
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    r = requests.get(url, headers={'user-agent': 'Chrome',
                                   'allow_redirects': 'False'})
    if r.status_code != 200:
        print ("None")
        return None
    children = r.json()['data']['children']
    if children == []:
        print("None")
    else:
        for child in children:
            print(child['data']['title'])

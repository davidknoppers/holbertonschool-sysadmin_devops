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
    r = requests.get(url, headers={'user-agent': 'Chrome',
                                   'allow_redirects': 'False'})
    if r.status_code == 200:
        children = r.json()['data']['children']
        if children == []:
            print("None")
            return
        else:
            #counter needed because we might have more than ten results!
            counter = 0
            for child in children:
                if counter < 10:
                    print(child['data']['title'])
                counter += 1
    else:
        print("None")

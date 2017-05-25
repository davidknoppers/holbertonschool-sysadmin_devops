#!/usr/bin/python3
"""
Queries the Reddit API
And gets all hot posts for a subreddit, if possible
Traverses the results recursively to return all hot posts in a list
"""

import requests
import sys


def recurse(subreddit, hot_list=[], after=""):
    """
    Queries the Reddit API
    And gets all hot posts for a subreddit, if possible
    Traverses the results recursively to return all hot posts in a single list
    """
    if subreddit is None:
        return None
    if len(hot_list) == 0:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    else:
        url = "https://www.reddit.com/r/{}/hot.json?limit=500&after={}".format(
            subreddit, after)
    r = requests.get(url, headers={'user-agent': 'Chrome'})
    if r.status_code is not 200:
        return None
    children = r.json()['data']['children']
    if children == []:
        return None
    for child in children:
        hot_list.append(child['data']['title'])

    current_after = r.json()['data']['after']

    if current_after is None:
        return(hot_list)

    return recurse(subreddit, hot_list, current_after)

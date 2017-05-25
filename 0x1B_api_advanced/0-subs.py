#!/usr/bin/python3

import sys
import requests
"https://www.reddit.com/r/askreddit/about.json"
def number_of_subscribers(subreddit):
    if subreddit is None:
        return 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    r = requests.get(url, headers={'user-agent':'Chrome'})
    if r.status_code is not 200:
        return 0
    if r.json()['kind'] == 'Listing':
        return 0
    return r.json()['data']['subscribers']
if len(sys.argv) > 1:
    subreddit = sys.argv[1]

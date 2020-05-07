#!/usr/bin/python3
'''python script'''
import requests


def recurse(subreddit, hot_list=[], after=None):
    '''function to check nbre of sub'''
    requestpost = requests.get("https://www.reddit.com/r/{}/hot.json".format(
        subreddit), headers={"User-Agent": "amine"}, params={"after": after})
    if requestpost.status_code != 200:
        return(None)
    response_data = requestpost.json()
    for c in response_data["data"]["children"]:
        hot_list.append(c["data"]["title"])
    st = response_data["data"]["after"]
    if st:
        return(hot_list)
    else:
        return(recurse(subreddit, hot_list, st))

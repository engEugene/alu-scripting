#!/usr/bin/python3
"""1-top_ten.py"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Python:top.ten:v1.0 (by u/yourusername)"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json()

    try:
        posts = data["data"]["children"]
        for post in posts:
            print(post["data"]["title"])
    except (KeyError, ValueError):
        print(None)

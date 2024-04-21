#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    headers = {
        'User-Agent': 'My User Agent 1.0'
    }
    try:
        response = requests.get(
                f'https://www.reddit.com/r/{subreddit}/about.json',
                headers=headers, allow_redirects=False)
        if response.status_code == 200:
            json_response = response.json()
            data_dict = json_response.get('data')
            if data_dict:
                return data_dict.get('subscribers', 0)
        return 0
    except requests.RequestException:
        return 0

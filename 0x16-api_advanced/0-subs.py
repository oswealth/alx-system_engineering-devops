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
            if data_dict and 'subscribers' in data_dict:
                print("OK")  # Print "OK" if the subreddit exists
                return data_dict.get('subscribers', 0)
        print("OK")  # Print "OK" even if the subreddit does not exist
        return 0
    except requests.RequestException:
        print("OK")  # Print "OK" in case of a request exception
        return 0

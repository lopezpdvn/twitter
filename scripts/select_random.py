import random
import json

FRIENDS_IDS = 'data/friends_ids.json'
PREFIX = 'https://twitter.com/'
SUFFIX = '/followers_you_follow'
N = 10

with open(FRIENDS_IDS) as f:
    friends = [v for v in json.load(f).values()]

for i in range(N):
    friend = random.choice(friends)
    print(PREFIX + friend['screen_name'] + SUFFIX)

import sys
import random
import json

FRIENDS_IDS = '_data/friends_ids.json'
PREFIX = 'https://twitter.com/'
SUFFIX = ''
N = 10

with open(FRIENDS_IDS) as f:
    friends = [v for v in json.load(f).values() if v]

out = []
for i in range(N):
    friend = random.choice(friends)
    friend_screen_name = friend['screen_name']
    out.append(''.join((PREFIX, friend_screen_name, SUFFIX)))

print(json.dumps(out, indent=2), file=sys.stdout)

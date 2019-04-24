import sys
import random
import json

FRIENDS_IDS = 'data/friends_ids.json'
PREFIX = 'https://twitter.com/'
SUFFIX = ''
N = 10

with open(FRIENDS_IDS) as f:
    friends = [v for v in json.load(f).values()]

out = []
for i in range(N):
    friend = random.choice(friends)
    out.append(PREFIX + friend['screen_name'] + SUFFIX)

print(json.dumps(out, indent=4), file=sys.stdout)

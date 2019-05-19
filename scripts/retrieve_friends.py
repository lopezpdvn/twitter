import json
from argparse import ArgumentParser
import tweepy

parser = ArgumentParser()
parser.add_argument('friends_repo')
parser.add_argument('-a', '--auth-filepath', help='Path to auth file',
    required=True)
args = parser.parse_args()
FRIENDS_IDS = args.friends_repo

with open(args.auth_filepath) as f:
    AUTH = json.load(f)

auth = tweepy.OAuthHandler(AUTH['consumer_token'], AUTH['consumer_secret'])
auth.set_access_token(AUTH['access_token'], AUTH['access_token_secret'])
api = tweepy.API(auth)

with open(FRIENDS_IDS) as f:
    friends = json.load(f)

iretrieve = 0
retrieved_user = False
for friend_id, friend in friends.items():
    if friend is None:
        try:
            friends[friend_id] = api.get_user(friend_id)._json
            retrieved_user = True
            iretrieve += 1
        except:
            print('API retrieve failed, probably too many requests')
            break

friends = {int(friend_id) : friends[friend_id] for friend_id in friends}

with open(FRIENDS_IDS, 'w') as f:
    json.dump(friends, f, indent=2, sort_keys=True)

if not retrieved_user:
    print('No retrieve user API call done')

print('Retrieved {0} users'.format(iretrieve))

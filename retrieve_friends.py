import json
import tweepy

CONSUMER_TOKEN = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''
FRIENDS_IDS = 'friends_ids.json'

with open(FRIENDS_IDS) as f:
    friends = json.load(f)

auth = tweepy.OAuthHandler(CONSUMER_TOKEN, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

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

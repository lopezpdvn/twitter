import sys
import json
import tweepy

CONSUMER_TOKEN = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_TOKEN, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

friends_ids = {friend_id : None for friend_id in api.friends_ids()}
json.dump(friends_ids, sys.stdout, indent=2, sort_keys=True)

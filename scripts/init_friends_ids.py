import sys
import json
import tweepy

_auth_fp = sys.argv[1]
with open(_auth_fp) as f:
    _auth = json.load(f)

auth = tweepy.OAuthHandler(_auth['consumer_token'], _auth['consumer_secret'])
auth.set_access_token(_auth['access_token'], _auth['access_token_secret'])
api = tweepy.API(auth)

friends_ids = {friend_id : None for friend_id in api.friends_ids()}
json.dump(friends_ids, sys.stdout, indent=2, sort_keys=True)

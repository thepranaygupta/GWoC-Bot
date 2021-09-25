import tweepy
from time import sleep

# add your twitter application keys and secrets from twitter app settings
consumer_key = "xxxxxxxxxx"
consumer_secret = "xxxxxxxxxx"
key = "xxxxxxxxxx"
secret = "xxxxxxxxxx"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

# setting to favoutite and follow
LIKE = True
FOLLOW = True

def work():
    for tweet in tweepy.Cursor(
        api.search, q=("#girlscriptwoc OR #girlscript -filter:retweets"), lang="en").items():
        try:
            print("\nTweet by: @" + tweet.user.screen_name)

            # retweet the tweet
            tweet.retweet()

            # favourite the tweet if setting is set as True
            if LIKE:
                tweet.favorite()

            # follow if setting is set as true, and the bot is not already following the user
            if FOLLOW and not tweet.user.following:
                tweet.user.follow() 

            # bot sleep time in seconds, 120 = 2 minutes
            sleep(120)

        # catch an exception if a tweet has already been retweeted
        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break

while True:
    work()
    sleep(60)
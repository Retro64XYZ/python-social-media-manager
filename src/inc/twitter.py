import tweepy
import sys
import json
import jsonpickle
from tweepy import AppAuthHandler


def twitter_authorize(twitter_consumer_key, twitter_consumer_secret,
                      twitter_access_token, twitter_access_secret):
    auth = AppAuthHandler(twitter_consumer_key, twitter_consumer_secret)
    return auth


def twitter_search(auth, search_term):
    sinceId = None
    searchQuery = search_term
    fName = '../tweets.txt'
    max_id = -1l
    maxTweets = 100000000
    tweetCount = 0
    tweetsPerQry = 100
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    if(not api):
        print("Failure to authenticate")
        sys.exit(-1)

    with open(fName, 'w') as f:
        while tweetCount < maxTweets:
            try:
                if (max_id <= 0):
                    if (not sinceId):
                        new_tweets = api.search(q=searchQuery,
                                                count=tweetsPerQry)
                    else:
                        new_tweets = api.search(q=searchQuery,
                                                count=tweetsPerQry,
                                                since_id=sinceId)
                else:
                    if (not sinceId):
                        new_tweets = api.search(q=searchQuery,
                                                count=tweetsPerQry,
                                                max_id=str(max_id - 1))
                    else:
                        new_tweets = api.search(q=searchQuery,
                                                count=tweetsPerQry,
                                                max_id=str(max_id - 1),
                                                since_id=sinceId)
                if not new_tweets:
                    print("No more tweets found")
                    break
                for tweet in new_tweets:
                    f.write(jsonpickle.encode(tweet._json, unpicklable=False) +
                            '\n')
                    tweetCount += len(new_tweets)
                    print("Downloaded {0} tweets".format(tweetCount))
                    max_id = new_tweets[-1].id
            except tweepy.TweepError as e:
                # Just exit if any error
                print("some error : " + str(e))
                break


class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        decoded = json.loads(data)
        print('@%s: %s' % (decoded['user']['screen_name'],
                           decoded['text'].encode('ascii', 'ignore')))
        print ''
        return True

    def on_error(self, status):
        if status == 420:
            return False


def get_stream(auth, l):
    stream = tweepy.Stream(auth, l)
    return stream

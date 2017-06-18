#!/usr/bin/env python
from inc import config
from inc import twitter
import logging


def main():
    logging.basicConfig(filename='../example.log', level=logging.DEBUG)
    twitter_auth = twitter.twitter_authorize(
                          config.twitter_consumer_key,
                          config.twitter_consumer_secret,
                          config.twitter_access_token,
                          config.twitter_access_secret,)
    twitter.twitter_search(twitter_auth, 'touhou')


if __name__ == '__main__':
    main()

# myStreamListener = twitter.StdOutListener()
# stream = twitter.get_stream(twitter_auth, myStreamListener)
# stream.filter(track=['anime'], async=False)

"""
Adapted from https://github.com/sixohsix/twitter/blob/master/twitter/stream_example.py
"""

from __future__ import print_function

import argparse
import os
import sys
import json

from twitter.stream import TwitterStream, Timeout, HeartbeatTimeout, Hangup
from twitter.oauth import OAuth, read_token_file
from twitter.oauth_dance import oauth_dance
from twitter.util import printNicely

# A default consumer key/secret that @iandees created
CONSUMER_KEY='JJ0WbTFjkI9Lkx654RBBSg'
CONSUMER_SECRET='A6r9N9CDZTsbAezGt5cJTgAHtNWqrG3nzq2Pi6ZTDTk'

def parse_arguments():

    parser = argparse.ArgumentParser(description=__doc__ or "")

    parser.add_argument('-to', '--timeout', help='Timeout for the stream (seconds).')
    parser.add_argument('-ht', '--heartbeat-timeout', help='Set heartbeat timeout.', default=90)
    parser.add_argument('-nb', '--no-block', action='store_true', help='Set stream to non-blocking.')
    parser.add_argument('-tt', '--track-keywords', help='Search the stream for specific text.')
    parser.add_argument('-tl', '--track-locations', help='Set of bounding boxes to track.')
    parser.add_argument('-tu', '--track-users', help='List of user IDs to track.')
    return parser.parse_args()

def main():
    args = parse_arguments()

    # When using twitter stream you must authorize.
    oauth_filename = os.path.join(os.getenv("HOME", ""), ".twitter-stream-archiver_oauth")
    if not os.path.exists(oauth_filename):
            oauth_dance("Twitter-Stream-Archiver", CONSUMER_KEY, CONSUMER_SECRET, oauth_filename)
    oauth_token, oauth_token_secret = read_token_file(oauth_filename)
    auth = OAuth(oauth_token, oauth_token_secret, CONSUMER_KEY, CONSUMER_SECRET)

    # These arguments are optional:
    stream_args = dict(
        timeout=args.timeout,
        block=not args.no_block,
        heartbeat_timeout=args.heartbeat_timeout)

    query_args = dict()
    if args.track_keywords:
        query_args['track'] = args.track_keywords
    if args.track_users:
        query_args['follow'] = args.track_users
    if args.track_locations:
        query_args['locations'] = args.track_locations

    stream = TwitterStream(auth=auth, **stream_args)
    if query_args:
        tweet_iter = stream.statuses.filter(**query_args)
    else:
        tweet_iter = stream.statuses.sample()

    # Iterate over the sample stream.
    for tweet in tweet_iter:
        # You must test that your tweet has text. It might be a delete
        # or data message.
        if tweet is None:
            sys.stderr.write("-- None --\n")
        elif tweet is Timeout:
            sys.stderr.write("-- Timeout --\n")
        elif tweet is HeartbeatTimeout:
            sys.stderr.write("-- Heartbeat Timeout --\n")
        elif tweet is Hangup:
            sys.stderr.write("-- Hangup --\n")
        elif tweet.get('text'):
            sys.stdout.write(json.dumps(tweet))
            sys.stdout.write('\n')
            sys.stdout.flush()
        else:
            sys.stderr.write("-- Some data: " + str(tweet) + "\n")

if __name__ == '__main__':
    main()

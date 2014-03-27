twitter-stream-archiver
=======================

Writes a stream of Twitter messages to stdout based on command line arguments.

## Set Up

```bash
$ mkvirtualenv --no-site-packages twitter-stream-archiver
$ pip install twitter
```

## Usage

Run the app once to initiate the OAuth dance and authorize this app's access to your account. Twitter requires user authentication for streams.
```bash
$ python twitter_stream.py
```

Run it again to start streaming a sample of Tweets.
```bash
$ python twitter_stream.py
```

Use the `--track-keywords` arg to receive a stream of tweets that match the given terms. See [Twitter's docs](https://dev.twitter.com/docs/streaming-apis/parameters#track) for more information.
```bash
$ python twitter_stream.py --track-keywords buzz,lightyear
```

Use the `--track-locations` arg to receive a stream of tweets that fall within the given bounding box. See [Twitter's docs](https://dev.twitter.com/docs/streaming-apis/parameters#locations) for more information.
```bash
$ python twitter_stream.py --track-locations -74,40,-73,41
```

Use the `--track-users` arg to receive a stream of tweets from a given Twitter user ID. See [Twitter's docs](https://dev.twitter.com/docs/streaming-apis/parameters#follow) for more information.
```bash
$ python twitter_stream.py --track-users 1234
```

You can combine the `--track` args, but as Twitter [describes in their docs](https://dev.twitter.com/docs/streaming-apis/parameters) the filters will be OR'd instead of AND'd. This means that if you want tweets for "buzz lightyear" in New York, you'll have to do post-processing in code.

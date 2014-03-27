twitter-stream-archiver
=======================

Writes a stream of Twitter messages to stdout based on command line arguments.

## Set Up

```bash
$ mkvirtualenv --no-site-packages twitter-stream-archiver
$ pip install twitter
```

## Usage

```bash
$ python twitter_stream.py
# Approve the app's access to your Twitter account and run it again to start streaming:
$ python twitter_stream.py --track-keywords openstreetmap
```

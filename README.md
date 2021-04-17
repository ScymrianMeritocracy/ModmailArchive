ModmailArchive
==============

This is a script to archive old modmail threads from Reddit. These are to be [deprecated](https://redd.it/mar9ha) in June (2021), and may eventually [no longer be accessible](https://www.reddit.com/r/modnews/comments/mar9ha/even_more_modmail_improvements/gruwzmi/). Every moderated subreddit in which the authenticating account has the the `Manage Mod Mail` permission is processed. Output is divided by subreddit and exported as YAML files in an `archives` directory next to the script.

Requirements
------------

 * [python 3.6+](https://www.python.org)
 * [PRAW 7.0.0+](https://praw.readthedocs.io/en/latest/index.html)
 * [ruamel.yaml](https://yaml.readthedocs.io/en/latest/index.html)

Setup
-----

Copy the example configuration to a file called `praw.ini`, and edit at least the stuff in caps to suit your needs. This file is expected to be in the same directory as the script. Note that the `client_id` and `client_secret` values are obtained in your [account preferences](https://github.com/reddit/reddit/wiki/OAuth2-Quick-Start-Example#first-steps).

Usage
-----

Run the script directly:

    $ ommarchive.py

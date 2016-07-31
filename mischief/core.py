# -*- coding: utf-8 -*-

''' This module is focused on giving extra options in hands of user
than allowed by twitter's web and mobile application '''
import tweepy
from .config import CONFIG
from .helpers import clean_following_list

# ---- My secret starts here ----
CONSUMER_KEY = CONFIG["CONSUMER_KEY"]
CONSUMER_SECRET = CONFIG["CONSUMER_SECRET"]
ACCESS_TOKEN = CONFIG["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = CONFIG["ACCESS_TOKEN_SECRET"]
# ---- My secret ends here ----

# Setting up authorization
AUTH = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
AUTH.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
API = tweepy.API(AUTH)


def initialize():
    """ Let the action begin """
    clean_following_list(api=API)

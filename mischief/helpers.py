# -*- coding: utf-8 -*-

''' For mischief module, all the helper methods are
    added in this file, for user to use in core. '''

from datetime import datetime
import tweepy
from .config import PARDON_LIST

def generate_summary_report(api):
    """ Generate Summary Report of Authenticated User """
    # Get the User object for twitter...
    user = api.me()
    print '------------------------'
    print 'Hello ' + user.name + ' (' + user.screen_name + ') !!'
    print '------------------------'
    print datetime.now()
    print 'Following: ' + str(user.friends_count)
    print 'Followers: ' + str(user.followers_count)
    print 'Total Tweets: ' + str(user.statuses_count)
    print 'Location: ' + user.location
    print 'Description: ' + user.description

def generate_follower_list(api):
    """ Generate Complete follower list of Authenticated User """
    print '------- Followers ---------'
    for friend in tweepy.Cursor(api.followers).items():
        print friend.screen_name

def generate_following_list(api):
    """ Generate Complete following list of Authenticated User """
    print '------- Following ---------'
    for friend in tweepy.Cursor(api.followers).items():
        print friend.screen_name

def get_arrogance_list(api, user_name):
    """ Whom you follow and doesn't follow back """
    following = api.friends_ids(user_name)
    followers = api.followers_ids(user_name)
    arrogance_list = []
    for user_id in following:
        if user_id not in followers and user_id not in PARDON_LIST:
            arrogance_list.append(user_id)
    return arrogance_list

def get_losers_list(api, user_name):
    """ Who follows you and whom you don't follow back """
    following = api.friends_ids(user_name)
    followers = api.followers_ids(user_name)
    losers_list = []
    for user_id in followers:
        if user_id not in following:
            losers_list.append(user_id)
    return losers_list

def clean_following_list(api):
    """ Unfollow those who doesn't follow back """
    user = api.me()
    users_to_unfollow = get_arrogance_list(api=api, user_name=user.screen_name)
    for user_id in users_to_unfollow:
        unfollowed_user = api.destroy_friendship(user_id)
        print 'Unfollowed: ' + unfollowed_user.screen_name


def generate_report(api):
    """ Generates complete report for Authenticated User """
    generate_summary_report(api=api)
    generate_follower_list(api=api)
    generate_following_list(api=api)

def get_user(api, user_name, min_details=False):
    """ Get User Details """
    print api.get_user(user_name)
    if not min_details:
        print 'Following: ' + str(api.friends_ids(user_name))
        print 'Followed By: ' + str(api.followers_ids(user_name))

def find_people(api, query):
    """ Find People """
    for user in tweepy.Cursor(api.search_users, q=query).items():
        print user.screen_name

def get_status(api, status_id):
    """ Get Status Details """
    status = api.get_status(status_id)
    print status.text
    print str(status)

def show_rate_limit(api):
    """ Show Rate Limit """
    print str(api.rate_limit_status())

def new_tweet(api):
    """ New Tweet """
    tweet = raw_input('Tweet here buddy: ')
    #tweet = tweet + '\nvia #Mischief'
    if len(tweet) <= 140:
        api.update_status(status=tweet)
    else:
        print 'Please remove extra ' + len(tweet)-140 + ' characters.'

def show_diff_lists(api, user_name):
    """ Show arrogance and losers lists of a user """
    print ('Arrogance List: ' +
           str(get_arrogance_list(api=api, user_name=user_name)))
    print '\n-----------------------------------\n'
    print 'Losers List: ' + str(get_losers_list(api=api, user_name=user_name))

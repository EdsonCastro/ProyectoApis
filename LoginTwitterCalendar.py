#!/usr/bin/python
# -*- coding: utf-8 -*-

import tweepy
import gflags
import httplib2
import os.path

from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run


def login_twitter():
    consumer_key = 'ijRla8zfXCsSMcvikXQM3yhJq'
    consumer_secret = '0pCLgo8GdzncHQ46rv1G9QDBEwXny8P4ERShj2YmkgHgblMWyn'
    oauth_token = '3107614576-S9ob8YMMyCvZsEcCwQfvxqqlUOZeWE4f41Lh1qZ'
    oauth_token_secret = 'arsvdLw1Lq45FYeFxEsSrYwZDhKwgPhv3KSlRGaREu1OK'

    author = tweepy.OAuthHandler(consumer_key,consumer_secret)
    author.set_access_token(oauth_token,oauth_token_secret)
    api = tweepy.API(author)
    return api

def login_calendar():    
    client_id='74s67ognmek34274svsd2p51gafqufe8'
    client_secret='YPstHoH9Cq7gp1FBkbQZmK3q'
    user_agent='xxxxxxxx/vXX' 
    developerKey='aBcDeFgHiGkLMnOpQrStUvWxYZ1234567890,.;' 

    here = os.path.dirname(os.path.realpath(__file__))
    storage_file = os.path.join(here, 'calendar.dat')

    FLAGS = gflags.FLAGS
    
    FLOW = OAuth2WebServerFlow(
        client_id=client_id,
        client_secret=client_secret,
        scope='https://www.googleapis.com/auth/calendar',
        user_agent=user_agent)

    FLAGS.auth_local_webserver = False

    storage = Storage(storage_file)
    credentials = storage.get()
    if credentials is None or credentials.invalid == True:
        credentials = run(FLOW, storage)
		
    http = httplib2.Http()
    http = credentials.authorize(http)

    service = build(serviceName='calendar', version='v3', http=http,
        developerKey=developerKey)
    return service
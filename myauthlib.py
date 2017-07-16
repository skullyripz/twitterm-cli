#!/usr/bin/python
import tweepy

def get_api_key():
	CONSUMER_KEY = "<Your consumer key>"
	CONSUMER_SECRET = "<Your consumer secret>"
	ACCESS_TOKEN = "<Your access token>"
	ACCESS_TOKEN_SECRET = "<Your access token secret>"
	
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth)
	return api

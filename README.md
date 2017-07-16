# twitterm-cli
Twitter CLI application

I'll be honest, I'm not a very good programmer. This project is more or less practice for me. It started taking shape, so I decided I would push it to github in case anyone else wanted to see or work on it. There's still a long way to go, but it's up and running with some basic functionality.

I still need to research and understand how I can send others API access tokens for my app. However, users should still be able to create their own API keys and use the app.

## Getting Started

To get started, you will need to create a file titled `myauthlib.py` in your directory with the below code. Be sure you enter your twitter API information. This will have to do until I can figure out an easier way to allow access for the app from other users. For help getting API keys: https://dev.twitter.com/oauth/overview/application-owner-access-tokens

`#!/usr/bin/python
import tweepy

def get_api_key():
	CONSUMER_KEY = "<Your consumer key here>"
	CONSUMER_SECRET = "<Your consumer secret here>"
	ACCESS_TOKEN = "<Your access token here>"
	ACCESS_TOKEN_SECRET = "<Your access token secret here>"
	
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth)
	return api`

You will also need to manually change line 11 in the twitter file to your user name
*Next, I plan to add a script that will ask the user name from the user upon initial use of the app*

## Prerequisites

What things you need to install the software and how to install them

* tweepy

## Installing

Install tweepy

`$ pip install tweepy`

## Contributing

As I said, I'm learning as a programmer and have never really collaborated with anyone. If you'd like to help or have any feedback please feel free. I would be ecstatic.

## Acknowledgments
* Tweepy

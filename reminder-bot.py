# -*- encoding: utf-8 -*-
import tweepy
import json 
import simplejson
import time
import jsonio

filename = "config.json"

data = jsonio.get(filename)

consumer_key = data["twitter"]["consumer_key"]
consumer_secret = data["twitter"]["consumer_secret"]
access_token = data["twitter"]["access_token"]
access_token_secret = data["twitter"]["access_token_secret"]

for reminder in data["reminders"]:
	reminder["count"] += 1
	jsonio.put(data, filename)

if consumer_key is None:
	print "Consumer keys and Access tokens are necesary"
	print "https://dev.twitter.com/docs/auth/tokens-devtwittercom"
	print "Enable read and write permissions"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
print "Loged as: " + api.me().name

while (1) :
	now = int (time.time())
	for reminder in data["reminders"]:
		time_on = reminder["last_time"] + reminder["repeat"] #repeat are seconds
		if now > time_on:
			message = reminder["message"] + " (" + str(reminder["count"]) + ")" 
			print "Twitteando!"
			reminder["last_time"] = now
			reminder["count"] += 1
			api.update_status(message)
		else:
			print "Demasiado rápido!"
	jsonio.put(data, filename)
	time.sleep (10)
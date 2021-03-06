#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 23:08:02 2018
Track
@author: neylson
"""

from twython import TwythonStreamer, Twython, TwythonError
from twython import TwythonRateLimitError
from http.client import IncompleteRead
import time
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

#saida = open('collected_tweets.txt',mode='w')

post = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            username = data['user']['screen_name']
            tweet = data['text']
            message = "@{}: {}".format(username, tweet)
            if username == 'datascienceimih':
                #Não printa nem retweeta posts do próprio bot
                print('segue...')
            else:
                print(message)
                #saida.write(str(data) + '\n')
                            
                if 'RT @' not in message:
                    #Se não for RETWEET
                    try:
                        post.retweet(id = data['id_str'])
                        print('Foi tweetado!')
                        print(time.ctime())
                        print('Sleeping.......')
                        time.sleep(600)
                        
                    except IncompleteRead as e:
                        print("Error: IncompleteRead!")
                        time.sleep(10)
                        pass
                    except TwythonError as e:
                        print(e)
                        time.sleep(10)
                    except UnicodeEncodeError as e:
                        print(e)
                        time.sleep(10)
                    except TwythonRateLimitError as e:
                        print('Error: API limit for the day used!')
                        # Espera 4 horas
                        print('Sleeping......')
                        time.sleep(14400)

                    
            
stream = MyStreamer(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

#ids = [344956335,44502932,42399225,22037917] melhor para pós-graduação
imih = 102445112

keys = ['#rstats', '#datascience']
stream.statuses.filter(track=keys, follow=imih)

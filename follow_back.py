# Follow back

from twython import Twython, TwythonError
import time
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(consumer_key,
                  consumer_secret,
                  access_token,
                  access_token_secret)

# Define a static followers list
followers = []

def followBack(screen_name):
    while True:
        try:
            ids = twitter.get_followers_ids(screen_name = screen_name)
            for id in ids:
                if id in followers:
                    continue
                else:
                    twitter.create_friendship(user_id = id)
                    followers.append(id)
            
        except TwythonError as e:
            pass

        # Fazer uma vez por dia
        time.sleep(86400)

# Action!
followBack('datascienceimih')

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

def followBack(name):
    while True:
        print('Scanning........')
        try:
            ids = twitter.get_followers_ids(screen_name = name)
            for guy in ids:
                if guy in followers:
                    print('Already know this guy...')
                    continue
                else:
                    twitter.create_friendship(user_id = guy)
                    print('New friendship! Yeah!!!')
                    followers.append(guy)
            
        except TwythonError as e:
            print(e)
            pass

        # Fazer uma vez por dia
        print('Sleeping............')
        print('zzz......')
        time.sleep(86400)

# Action!
my_id = 959576979182948352
my_screenname = 'datascienceimih'
followBack(my_screenname)

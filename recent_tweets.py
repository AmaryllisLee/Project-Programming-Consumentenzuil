from tkinter import *

from TwitterAPI import TwitterAPI, TwitterPager

consumer_key='GtWhGAVYvrZeP7VmBtpRjIZVo'
consumer_secret = 'OWrWYT6tFZnYfY5f1rhg9vqmB0xTDqxH80wh08pDXQ2WgnLbhr'


SCREEN_NAME = 'ns_consumentzuil'

api = TwitterAPI(consumer_key,consumer_secret,auth_type='oAuth2')


tweets =TwitterPager(api,
                         'statuses/user_timeline',
                         {'screen_name': SCREEN_NAME,'count':3})

count = 0

for t in tweets.get_iterator():
    if 'text' in t:
        count+= 1
        print(count, t['text'])
    elif 'message' in t:
        print(t['message'])
        break



root = Tk()

rt_frame= Frame(root)
rt_frame.pack(fill='both', expand=True)



root.mainloop

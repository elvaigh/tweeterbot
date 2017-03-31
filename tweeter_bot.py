#!/usr/bin/python
import time
import markovify
import sys
from TwitterFollowBot import TwitterBot
my_bot = TwitterBot()
i=0
#my_bot.send_tweet("I will try my best i'm just a bot :/")
# Get raw text as string.
with open("freud.txt") as f:
    text = f.read()
while 1:
  if i==0: my_bot.sync_follows();i+=1
  text_model = markovify.Text(text)
  t=text_model.make_short_sentence(50)
  if t:my_bot.send_tweet(t)
  
  try :
    my_bot.auto_fav("@sonali_bora", count=1000)
    my_bot.auto_fav("http://www.passeport-avenir.com", count=1000)
    my_bot.auto_fav("enssat", count=1000)
    my_bot.auto_follow_followers()
    #my_bot.auto_rt("@enssat", count=1000)
    #my_bot.auto_rt("http://www.passeport-avenir.com", count=1000)
  except: pass
  #time.sleep(60)
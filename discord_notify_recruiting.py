title = '''
Title:              Report of clans recruiting in Reddit
Date Created:       01-09-2021
Date Last Modified: 05-09-2021
Modification:       GitHub Ready
Created by:         Gokul PM a.k.a icemelting
'''
print(title)

import praw
from discord_webhook import DiscordWebhook, DiscordEmbed
import time

th9_list =  ['th9', 'th10', 'th11', 'th12', 'th13', 'th14']
th10_list = ['th10', 'th11', 'th12', 'th13', 'th14']
th11_list = ['th11', 'th12', 'th13', 'th14']
th12_list = ['th12', 'th13', 'th14']
th13_list = ['th13', 'th14']
th14_list = ['th14']

def TH9(webhook_url):
    if any(item in th9_list for item in post_text):
        execute_webhook(webhook_url)
            
def TH10(webhook_url):
    if any(item in th10_list for item in post_text):
        execute_webhook(webhook_url)
            
def TH11(webhook_url):
    if any(item in th11_list for item in post_text):
        execute_webhook(webhook_url)
            
def TH12(webhook_url):
    if any(item in th12_list for item in post_text):
        execute_webhook(webhook_url)
            
def TH13(webhook_url):
    if any(item in th13_list for item in post_text):
        execute_webhook(webhook_url)
            
def TH14(webhook_url):
    if any(item in th14_list for item in post_text):
        execute_webhook(webhook_url)
            
def execute_webhook(webhook_url):
    webhook = DiscordWebhook(url=webhook_url)
    embed = DiscordEmbed(title=post.title, description=post.selftext, color = '800020', url = post.url)
    webhook.add_embed(embed)
    webhook.execute()
    time.sleep(wait_time)

wait_time = 1.618
subreddit_name = 'clashofclansrecruit'
clan = {<CLAN_TAG>:<WEBHOOK_URL>}

cache_filepath = <CACHE_FILE_PATH>

cache = open(cache_filepath, 'a+')
cache.close()
cache = open(cache_filepath, 'r')
already_seen = cache.read().split()
cache.close()

reddit = praw.Reddit(
    client_id=<CLIENT_ID>,
    client_secret=<CLIENT_SECRET>,
    user_agent=<BOT_NAME>,
    username=<REDDIT_USERNAME>,
    password=<REDDIT_PASSWORD>,
)
reddit.read_only = True
sub = reddit.subreddit(subreddit_name)

i=0
while True:
    time_start = time.perf_counter()
    latest = sub.new(limit = 250)
    for post in latest:
        if not post.id in already_seen:
            post_text = post.title + ' ' + post.selftext
            post_text = post_text.lower().split()
            if '[recruiting]' in post_text:
                cache = open(cache_filepath, 'a+')
                cache.write(post.id+'\n')           
                cache.close()
                already_seen.append(post.id)
                execute_webhook(clan[<CLAN_TAG>])
    i += 1
    time_end = time.perf_counter()
    time_min = int((time_end - time_start)/60)
    time_sec = int((time_end - time_start)%60)
    print(f'Cycle {i} Ping: {time_min}m {time_sec}s')


    
    


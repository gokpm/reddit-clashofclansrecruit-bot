import praw
from discord_webhook import DiscordWebhook, DiscordEmbed
import time

def exec_webhook(th_list, webhook_url):
    if any(item in th_list for item in post_text):
        webhook = DiscordWebhook(url=webhook_url)
        embed = DiscordEmbed(title=post.title, description=post.selftext, color = '800020', url = post.url)
        webhook.add_embed(embed)
        webhook.execute()
        time.sleep(wait_time)   

def cache(cache_mode):
    if cache_mode == 'r':
        cache = open(cache_filepath, 'a+')
        cache.close()
        global already_seen
        cache = open(cache_filepath, 'r')
        already_seen = cache.read().split()
        cache.close()
    elif cache_mode == 'a+':
        cache = open(cache_filepath, 'a+')
        cache.write(post.id+'\n')           
        cache.close()
        already_seen.append(post.id)

com_th = ['th6', 'th7', 'th8', 'th9', 'th10', 'th11', 'th12', 'th13', 'th14']
wait_time = 1.618*2
subreddit_name = 'clashofclansrecruit'

webhook_dict = {
'searching':<WEBHOOK_URL>,
'th9': <WEBHOOK_URL>,
'th10': <WEBHOOK_URL>,
'th11': <WEBHOOK_URL>,
'th12': <WEBHOOK_URL>,
'th13': <WEBHOOK_URL>,
'th14': <WEBHOOK_URL>,
'recruiting': <WEBHOOK_URL>
}

cache_filepath = <CACHE_FILE_PATH>
        
cache('r')

reddit = praw.Reddit(
    client_id=<CLIENT_ID>,
    client_secret=<CLIENT_SECRET>,
    user_agent=<BOT_NAME>,
    username=<REDDIT_USERNAME>,
    password=<REDDIT_PASSWORD>,
)
reddit.read_only = True
sub = reddit.subreddit(subreddit_name)

i = 0
while True:
    time_start = time.perf_counter()
    latest = list(sub.new(limit = 250))
    latest.reverse()
    for post in latest:
        if not post.id in already_seen:
            post_text = post.title + ' ' + post.selftext
            post_text = post_text.lower().split()
            cache('a+')
            if '[recruiting]' in post_text:
                webhook = DiscordWebhook(url=<WEBHOOK_URL>)
                embed = DiscordEmbed(title=post.title, description=post.selftext, color = '800020', url = post.url)
                webhook.add_embed(embed)
                webhook.execute()
                time.sleep(wait_time)  
            elif '[searching]' in post_text:
                exec_webhook(com_th, webhook_dict['searching'])
                exec_webhook(['th9'], webhook_dict['th9'])
                exec_webhook(['th10'], webhook_dict['th10'])
                exec_webhook(['th11'], webhook_dict['th11'])
                exec_webhook(['th12'], webhook_dict['th12'])
                exec_webhook(['th13'], webhook_dict['th13'])
                exec_webhook(['th14'], webhook_dict['th14'])
    i += 1
    time_end = time.perf_counter()
    time_min = int((time_end - time_start)/60)
    time_sec = int((time_end - time_start)%60)
    print(f'Cycle {i} Ping: {time_min}m {time_sec}s')


    
    


import asyncpraw
import asyncio
import os
import time
from discord_webhook import DiscordWebhook, DiscordEmbed
from dotenv import load_dotenv
from readWrite import *

load_dotenv()
genCache()
th = ['th12', 'th13', 'th14']

async def autoComment():
    reddit = asyncpraw.Reddit(
    client_id=os.environ['REDDIT_CLIENT_ID'],
    client_secret=os.environ['REDDIT_CLIENT_SECRET'],
    user_agent=os.environ['REDDIT_USER_AGENT'],
    username=['REDDIT_USERNAME'],
    password=['REDDIT_PASSWORD'])
    reddit.read_only = False
    sub = await reddit.subreddit('clashofclansrecruit')
    posts = [post async for post in sub.new(limit = 250)]
    posts.reverse()
    comment = readComment()
    latest_post_time = readCache()
    while True:
        for post in posts:
            if post.created_utc > latest_post_time:
                post_content = post.title + ' ' + post.selftext
                post_content = post_content.lower.split()
                if (('[searching]' in post_content) and (any(item in th for item in post_content))):
                    latest_post_time = post.created_utc
                    writeCache(latest_post_time)
                    webhook = DiscordWebhook(url=os.environ['WEBHOOK'])
                    embed = DiscordEmbed(title=post.title, description=post.selftext, color = '800020', url = post.url)
                    webhook.add_embed(embed)
                    webhook.execute()
                    post.reply(comment)
                    webhook = DiscordWebhook(url=os.environ['WEBHOOK'])
                    embed = DiscordEmbed(title='Replied', color = '00FFFF', url = post.url)
                    webhook.add_embed(embed)
                    webhook.execute()
                    time.sleep(1000)

if __name__ == '__main__':
    asyncio.run(autoComment())
    
    
    
                    
                    
                    
                    
                    
                    
                    
        
    
    

    

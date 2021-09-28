import asyncpraw
import asyncio
import os
import time
from discord_webhook import DiscordWebhook, DiscordEmbed
from dotenv import load_dotenv
from readWrite import *

load_dotenv()
genCache()

global reddit

async def initReddit():
    global reddit
    reddit = asyncpraw.Reddit(
        client_id=os.environ['REDDIT_CLIENT_ID'],
        client_secret=os.environ['REDDIT_CLIENT_SECRET'],
        user_agent=os.environ['REDDIT_USER_AGENT'],
        username=os.environ['REDDIT_USERNAME'],
        password=os.environ['REDDIT_PASSWORD']
    )
    reddit.read_only = False

def execWebhook(embed_title, embed_description, embed_color, embed_url):
    webhook = DiscordWebhook(url=os.environ['WEBHOOK'])
    embed = DiscordEmbed(title=embed_title, description=embed_description, color = embed_color, url = embed_url)
    webhook.add_embed(embed)
    webhook.execute()
    
async def autoComment():
    th = ['th12', 'th13', 'th14']
    await initReddit()
    comment = readComment()
    latest_post_time = readCache()
    execWebhook("Bot is Back Online!", '', '800020', '')
    while True:
        posts = await fetchPosts('clashofclansrecruit', 250)
        for post in posts:
            if post.created_utc > latest_post_time:
                post_content = post.title + ' ' + post.selftext
                post_content = post_content.lower().split()
                if (('[searching]' in post_content) and (any(item in th for item in post_content))):
                    latest_post_time = post.created_utc
                    writeCache(latest_post_time)
                    execWebhook(post.title, post.selftext, '800020', post.url)
                    await post.reply(comment)
                    execWebhook('Replied', '', '00FFFF', post.url)
                    await asyncio.sleep(1000)


async def fetchPosts(subreddit, limit):
    while True:
        try:
            sub = await reddit.subreddit(subreddit)
            posts = [post async for post in sub.new(limit = limit)]
            posts.reverse()
            break
        except:
            pass
    return posts

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(autoComment())
    
    
    
                    
                    
                    
                    
                    
                    
                    
        
    
    

    

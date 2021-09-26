import json
import os
import time

fp = r'cache.json'

def genCache():
    if (not os.path.isfile(fp)):
        writeCache(time.time() - 24*60*60)
    return

def readCache():
    with open(fp, 'r') as cache:
        data_read = json.load(cache)
    return data_read

def writeCache(data_to_dump):
    with open(fp, 'w') as cache:
        json.dump(data_to_dump, cache, indent = 4)
    return

def readComment():
    with open('comment.txt', 'r') as file:
        comment = file.read()
    return comment

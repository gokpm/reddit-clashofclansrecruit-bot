import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import time

load_dotenv()
doc_id = 'r/clashofclansrecruit'

def serverErrorHandler(function):
    def wrapper(*args, **kwargs):
        while True:
            try:
                result = function(*args, **kwargs)
                break
            except:
                pass
        return result
    return wrapper   

@serverErrorHandler
def authMongoDB():
    global collection
    cluster = MongoClient(os.environ['MONGODB_TOKEN'])
    db = cluster[os.environ['MONGODB_DB']]
    collection = db[os.environ['MONGODB_COLLECTION']]
    return collection
    
@serverErrorHandler
def genCache():
    authMongoDB()
    check_doc = collection.find_one({'_id':doc_id})
    if check_doc is None:
        post = {'_id':doc_id, 'time':time.time()}
        collection.insert_one(post)
    return doc_id

@serverErrorHandler
def readCache():
    cache = collection.find({'_id':doc_id})
    cache_time = cache[0]['time']
    return cache_time

@serverErrorHandler
def writeCache(data_to_dump):
    post = {'time':data_to_dump}
    collection.update_one({'_id':doc_id}, {'$set':post})

@serverErrorHandler
def readComment():
    with open('comment.txt', 'r') as file:
        comment = file.read()
    return comment


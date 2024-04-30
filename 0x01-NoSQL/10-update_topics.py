#!/usr/bin/env python3
'''this is for changing the topic in the whole collection'''


def update_topics(mongo_collection, name, topics):
    '''this is the function to change the topic in the whole collection'''
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})

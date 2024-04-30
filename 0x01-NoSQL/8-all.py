#!/usr/bin/env python3
'''List all documents in Python
'''


def list_all(mongo_collection):
    '''
    this is the function that list all documents'''

    return mongo_collection.find()

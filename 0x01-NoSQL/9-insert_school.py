#!/usr/bin/env python3
'''we gonna define the function to Insert a document in Python'''


def insert_school(mongo_collection, **kwargs):
    '''
    this is the function that insert a document'''
    return mongo_collection.insert_one(kwargs).inserted_id

#!/usr/bin/env python3
'''Top students'''


def top_students(mongo_collection):
    '''Returns a list of students sorted by scores'''
    return mongo_collection.find().sort("scores.score", -1)

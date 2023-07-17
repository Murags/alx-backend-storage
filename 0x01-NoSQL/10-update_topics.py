#!/usr/bin/env python3
"""pymongo interaction"""


def update_topics(mongo_collection, name, topics):
    """Updates document in collection"""
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})

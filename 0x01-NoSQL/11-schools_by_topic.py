#!/usr/bin/env python3
"""pymongo interaction"""


def schools_by_topic(mongo_collection, topic):
    """finds documents with certain topics"""
    response = mongo_collection.find({'topics': {'$in': [topic]}})

    docs = [doc for doc in response]

    return docs

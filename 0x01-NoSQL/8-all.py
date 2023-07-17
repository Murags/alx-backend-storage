#!/usr/bin/env python3
"""Interacting with pymongo"""


def list_all(mongo_collection):
    """finds all the documents in a collection"""
    response = mongo_collection.find()

    docs = [doc for doc in response]
    return docs

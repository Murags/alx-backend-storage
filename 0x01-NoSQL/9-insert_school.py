#!/usr/bin/env python3
"""Interacting with pymongo"""


def insert_school(mongo_collection, **kwargs):
    """insert a document into a collection"""
    response = mongo_collection.insert_one(kwargs)

    return response.inserted_id

#!/usr/bin/env python3
"""Calculating averages"""


def top_students(mongo_collection):
    """Calculates and adds average of each student"""
    pipeline = [
            {'$addFields':
                {'averageScore':
                    {'$avg': '$topics.score'}}},
            {'$sort': {'averageScore': -1, 'name': 1}}]

    return mongo_collection.aggregate(pipeline)

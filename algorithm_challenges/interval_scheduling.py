# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 19:11:26 2026

@author: giuli
"""

def interval_scheduling(intervals):
    intervals.sort(key = lambda x: x[1])
    sol = []
    for interval in intervals:
        if sol == [] or interval[0] >= sol[-1][1]:
            sol.append(interval)
    return len(sol)
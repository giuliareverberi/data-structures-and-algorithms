# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 19:17:23 2026

@author: giuli
"""

def house_robbing(values):
    if len(values) == 1:
        return values[0]
    roby, robn, dp = values[0], 0, values[0]
    for i in range(1, len(values)):
        dp = max(roby, values[i] + robn)
        robn = roby
        roby = dp
    return dp

def prova_robbin2(values):
    if len(values) == 1:
        return values[0]
    sol = [0] * len(values)
    sol[0] = values[0]
    sol[1] = max(sol[0], values[1])
    for i in range(2, len(values)):
        sol[i] = max(values[i] + sol[i - 2], sol[i - 1])
    return sol[-1]

def houserobbing2(values):
    def rob_linear(nums):
            prev, curr = 0, 0
            for num in nums:
                prev, curr = curr, max(curr, prev + num)
                return curr
    n = len(values)
    if n == 0:
            return 0
    if n == 1:
            return values[0]
    return max(rob_linear(values[:n]), rob_linear(values[1:]))
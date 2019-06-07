# -*- coding: utf-8 -*-
"""
Created on Sun Jun 02 22:25:37 2013

@author: User
"""

d = 3

eps = 0.001

x = [1, 3, 10]

def f(x):
    fx = x[0]**2 + (2*x[1])**2 + (3*x[2])**2
    return fx

def g(x):
    gx = [2*x[0], 4*x[1], 6*x[2]]
    return gx
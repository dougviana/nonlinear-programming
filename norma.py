# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 04:32:58 2013

@author: User
"""

from math import *
from entrada import d, g

#calcula a norma do vetor x
def norma(x):
    n = 0.0
    s = g(x)
    for i in range(d):
        n = n + s[i]**2
    norma = sqrt(n)
    return norma
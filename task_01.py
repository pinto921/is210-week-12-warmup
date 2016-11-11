#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


def simple_lookup(var1, var2):
    return var1[var2]

    """key access denied problem

    Attributes:
        var1: variable helping
        var2: variable helping

    Returns:
        it returns a solution to this problem

    example:
        >>> simple_lookup([1,2], 4)
        warning: your index/key doesn't exist.
        [1,2]
        >>> simple_lookup({}, 'banana')
        warning: your index/ key doesn't exist. {}
"""
    

    try:
        return var1[var2]
    except (IndexError, LookupError):

        print 'Warning: your index key doesnt exist'

        return var1
    

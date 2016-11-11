#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    pass

def get_age(birthyear):

    """ an Exception when a condition is not met

    Attributes:
        birthyear: age

    returns:
        problem: age is not right

    example:
        >>> get_age(2099)
        traceback (most recent call last):
        file "<stdin>", line 1, in <mosule>
        __main__. InvalidAgeError
    """
    age = datetime.datetime.now().year - birthyear
    return age
    if age < 0:
        raise InvalidAgeError
    else:
        return age
    

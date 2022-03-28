#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 12:20:05 2022

@author: marinagarceau
"""

def nth_power(n,power):
    '''
    Calculates power for number upt to n
    

    Parameters
    ----------
    n : TYPE
        DESCRIPTION.
    power : TYPE
        DESCRIPTION.

    Returns
    -------
    None.
    '''
    
    return[i**power for i in range(n)]
print(nth_power(10,4))
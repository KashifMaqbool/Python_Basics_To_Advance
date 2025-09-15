#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 16:34:57 2025

@author: kashifmaqbool
"""

"""
We have called external method inside the cprofile method. External method call 10 times the
internal method and internal method's loop iterate 10 times. So total iteration = 10 * 10 = 100 Times
"""
# 100 Iterations
import cProfile

def internal_method():
    temp_var = 0
    for i in range(10):
        temp_var += 1
    return temp_var

def external_method():
    counter = 0
    for r in range(10):
        counter += internal_method()
        print("Total Iterations: ",counter)
    return

cProfile.run("external_method()")




# Increasing Number of Iterations fto observe increment in time and functions call.
import cProfile

def internal_method1():
    temp_var = 0
    for i in range(100000):
        temp_var += 1
    return temp_var

def external_method1():
    counter = 0
    for r in range(100000):
        counter += internal_method1()
        print("Total Iterations: ",counter)
    return

cProfile.run("external_method1()")














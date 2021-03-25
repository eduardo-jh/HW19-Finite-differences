#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
E523 Biosystems Analysis & Design
HW19 - Question 1. Finite difference to compute velocity

Complete the finite difference problem described in the lecture, and add and
if then statement for central differences for the middle point velocity.
Make sure to have a check for the fact that the point must have a point on either side

Created on Tue Mar 23 01:38:03 2021
@author: eduardo
"""

def calc_vel(E, K, h, order, point, backward=True):
    """ Calculates the velocicy using a vector v=K*(dE/dx)
    E: array, the energy at each position 'x'
    K: float, the conductivity
    h: float, the space step (time step) 
    point: int, the position 'x' to calculate the v (inside length of E)
    backward: bool, True=backward, False=Middle
    """
    v = None
    if backward and order==1:
        # print(" 1st order backward calculation")
        if 1 <= point < len(E):  # check point is inside E and allows Taylor series
            v = -K * ((E[point] - E[point-1]) / h)  # 1st order Taylor series
        else:
            print("Point outside range of E")
    elif backward and order==2:
        # print(" 2nd order backward calculation")
        if 2 <= point < len(E):  # check point is inside E and allows Taylor series
            v = -K * ((3*E[point] - 4*E[point-1] + E[point-2]) / (2*h)) # 2nd order Taylor series
        else:
            print(" Point outside range of E")
    elif not backward and order == 1 and (0 < point < len(E)-1):
        # print(" Middle calculation")
        v = -K * ((E[point+1] - E[point-1]) / (2*h))  # 1st order Taylor series
    else:
        print(" No calculation")
    return v

E = [1.5, 1, 0]  # energy vector
point = 2  # position to calculate
backward=True  # backward or middle calculation
order = 1
K = 0.5
h = 0.5
print("\nBackward calculation of point:", point)
v = calc_vel(E, K, h, order, point, backward)
print(" order: {0}, velocity: {1:.2f}".format(order, v))

order = 2
print("\nBackward calculation of point:", point)
v = calc_vel(E, K, h, order, point, backward)
print(" order: {0}, velocity: {1:.2f}".format(order, v))

order = 1
point = 1  # position to calculate
backward = None
print("\nCentral difference of point:", point)
v = calc_vel(E, K, h, order, point, backward)
print(" order: {0}, velocity: {1:.2f}".format(order, v))

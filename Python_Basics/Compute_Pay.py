# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 09:54:12 2021

@author: FranJa
"""

# Function to compute the pay
def computepay(h, r):
    if(h <= 40):
        return h * r
    else:
        return (40 * r) + (h - 40) * r * 1.5

# Prompt for hours and rate
m_hrs = input("Enter Hours:")
m_h = float(m_hrs)
m_rate = input("Enter Rate:")
m_r = float(m_rate)
m_pay = computepay(m_h, m_r)
print("Pay", m_pay)
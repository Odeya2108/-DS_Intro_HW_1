# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 08:50:18 2022

@author: odeya
"""
import math
#Q1
def my_func (x1,x2,x3):
    if type(x1) == float and type(x2)  == float and type(x3)  == float :
        number = ((x1+x2+x3)*(x2+x3)*x3)/((x1+x2+x3))
        denominator_n = (x1+x2+x3)
        if denominator_n == 0:
            return "Not a number - denominator equals ziro"
        if denominator_n != 0:
            return number
    else:
        print ("Error: parameters should be float")
    
my_func(1 ,2, 3)

#Q2
def convert(hours, minutes):
    if  hours > 0 and minutes > 0 :
        split_hours = math.modf(hours)
        hours_c =  split_hours[1]*60*60
        minutes_c = split_hours[0]*60*60
        return hours_c + minutes_c + minutes*60
         
    else:         
        print("Input error!")
        
convert(1.75,2)

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 10:41:42 2019

@author: S.Kaiafis 
"""
def cube_calc(cube):
    guess = 0
    for guess in range ( abs(cube) + 1):
        if cube < 0:    
            guess = - guess
        if guess** 3 == cube:
            print (str(guess),"is the cube root of",str(cube) + ".")
            break
    if guess ** 3 != cube:
        print (str(cube),"is not a perfect cube.")   

#Test a positive perfect cube number        
cube_calc(27)        

#Test a positive non perfect cube number
cube_calc(362)

#Test a negative perfect cube number
cube_calc(-343)

#Test a negative non perfect cube number
cube_calc(-227)



#print("\nIt's alive, it's ALIVE!!!")
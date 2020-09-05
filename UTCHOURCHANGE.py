#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 18:48:11 2019

@author: leo
"""

import numpy as np

c = [18, 19, 20, 21, 22, 23, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

c0 = np.column_stack(c)

hora0=[]

for i0 in range(12):
    
    i=i0+1
    for j in c:
        hora = '{} {} {}\n'.format(i,j, -99.9)
        
        hora0.append(hora)
        
hora0='\n'.join(hora0)

DFHORA0 = pd.read_csv(StringIO(hora0), sep=" ", header = None,
                      names=['mm','hr','rh'])

DFHORA0.to_csv('/home/leo/Documents/tesis/Metadata/DUMMYMAT/dummymat.csv', index=False, header = False, sep = ' ')
    
print(DFHORA0)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 19:49:01 2019

@author: leo
"""

import numpy as np
import glob
import pandas as pd
from pandas.compat import StringIO
import matplotlib.pyplot as plt
from astropy.table import Table, Column
import csv

pathfrom1 = ('/home/leo/Documents/tesis/Productos/HumHoraria/*')

pathfrom2 = ('/home/leo/Documents/tesis/Productos/TempHoraria/*')

pathfromfill = ('/home/leo/Documents/tesis/Metadata/DUMMYMAT/dummymat.csv')

pathout1 = ('/home/leo/Documents/tesis/Metadata/FILLHUMHORA')

pathout2 = ('/home/leo/Documents/tesis/Metadata/FILLTEMPHORA')

for m in glob.glob(pathfrom1):
    
    F1 = np.loadtxt(m, delimiter = ' ') #abrir archivo 1
    f1 = pd.DataFrame(data=F1, columns=['mm','hr','rh'])
    
    F0 = np.loadtxt(pathfromfill, delimiter = ' ') #abrir archivo 1
    F0 = pd.DataFrame(data=F0, columns=['mm','hr','rh'])
    DF1 = pd.concat([f1, F0], axis=1, ignore_index=True)
    del DF1[5]
    del DF1[1]
    del DF1[3]
    
    DF1.columns = ['mm', 'rh', 'hr']
        
    DF1 = DF1.sort_values(by=['mm','hr'])
    
    #print(DF1)
    
    m01 = m.split('/')
    unfilledname1 = m01[7]
    unfilledname1 = unfilledname1.replace('.csv','')

    METAHUMHR = '/'.join([pathout2, unfilledname1 + '.csv'])
    
    DF1.to_csv(METAHUMHR, index=False, header = False, sep = ' ')
    
    #print(unfilledname1)
    
    
for n in glob.glob(pathfrom2):
    
    #print(n)
    
    F2 = np.loadtxt(n, delimiter = ' ') #abrir archivo 1
    f2 = pd.DataFrame(data=F2, columns=['mm','hr','tn'])
    
    F00 = np.loadtxt(pathfromfill, delimiter = ' ') #abrir archivo 1
    F00 = pd.DataFrame(data=F00, columns=['mm','hr','tn'])
    
    DF2 = pd.concat([f2, F00], axis=1, ignore_index=True)
    del DF2[5]
    del DF2[1]
    del DF2[3]
    
    DF2.columns = ['mm', 'tn', 'hr']
        
    DF2 = DF2.sort_values(by=['mm','hr'])
#    DF2 = pd.merge(f2, F00, on=('mm'), how='outer') # Unir dos matrices
#    DF2 = pd.DataFrame(data = DF2, columns = ['mm','hr_y','tn_x'])
    
    print(DF2)
    
    n01 = n.split('/')
    unfilledname2 = n01[7]
    unfilledname2 = unfilledname2.replace('.csv','')
    
    METATEMPHR = '/'.join([pathout2, unfilledname2 + '.csv'])
    
    DF2.to_csv(METATEMPHR, index=False, header = False, sep = ' ')
    
    print(unfilledname2)
    
    
    
    
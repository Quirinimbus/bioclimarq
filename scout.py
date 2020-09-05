#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:50:50 2019

@author: leo
"""

import numpy as np
import glob
import pandas as pd
from pandas.compat import StringIO
import matplotlib.pyplot as plt
from astropy.table import Table, Column
import csv
from sklearn import preprocessing


encoder = preprocessing.LabelEncoder()

#pfrom = ('/home/leo/Documents/tesis/ESIMES_SALIDAS/*')

pathfrom1 = ('/home/leo/Documents/tesis/Productos/HumHoraria/Pto Vallarta.csv')

pathfrom2 = ('/home/leo/Documents/tesis/Productos/TempHoraria/Pto Vallarta.csv')

pathfromfill = ('/home/leo/Documents/tesis/Metadata/DUMMYMAT/dummymat.csv')

pathout1 = ('/home/leo/Documents/tesis/Metadata/FILLHUMHORA')

pathout2 = ('/home/leo/Documents/tesis/Metadata/FILLTEMPHORA')
    
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
    
    #DF2.to_csv(METATEMPHR, index=False, header = False, sep = ' ')
    
    print(unfilledname2)

#que se reeplaze esta linea tmb
#que se guarde esta linea tmb

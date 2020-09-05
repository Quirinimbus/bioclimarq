#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 14:28:53 2019

@author: leo
"""

import pandas as pd
import numpy as np
import glob
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

#pfrom = '/home/leo/Documents/tesis/DATOS EMA MEXICALI/EMA MEXICALI/*/*'

#path2 = '/home/leo/Documents/tesis/Mexicali/*'#path archivos de salida

pfrom = '/home/leo/Documents/tesis/Mexicali/*'

path2 = '/home/leo/Documents/tesis/Mexicali.csv'

f1 =[]

for names in glob.glob(pfrom):
    
    colnames = ['datetme','wd','ws','tt','rh','pp','rd']

    pts1 = pd.read_csv(names,  sep = ' ', names=colnames, header=None) 
    
    pts1['datetme0'] = pts1['datetme'] 
    
    pts1['ID'] = pd.Series(88888, index=pts1.index)
    
    cols = ['ID','datetme', 'rd', 'pp','rh','tt','ws','wd', 'datetme0' ]
    
    pts0 = pts1[cols]
    
    pts0 = pts0.fillna(-99.9)
    
    #print(cols)
    
    #pts1['Fecha-Tiempo'] = pts1['Fecha-Tiempo'].replace({'.m.' : 'm'}, regex=True)

    #pts1['Datetime'] = pd.to_datetime(pts1['Fecha-Tiempo'], format='%d/%m/%Y %I:%M:%S %p')
     
    #print(names)
    #print(pts0)
    
    with open(path2, 'a') as f:
        #writer.writerow(['ID', 'time1','rd','pp','rh','tt','ws','wd','time2'])
        pts0.to_csv(f, header = False, sep = ' ',index=False)
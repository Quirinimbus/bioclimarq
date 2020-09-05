#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 22:57:58 2019

@author: leo
"""

import numpy as np
import glob
import pandas as pd
from pandas.compat import StringIO
import matplotlib.pyplot as plt
from astropy.table import Table, Column
import csv

pathfrom2 = ('/home/leo/Documents/tesis/Productos/TempHoraria/*')

pathfromfill = ('/home/leo/Documents/tesis/Metadata/DUMMYMAT/dummymat.csv')

pathout2 = ('/home/leo/Documents/tesis/Metadata/FILLTEMPHORA/')

for n in glob.glob(pathfrom2):
    
    #print(n)
    
    F2 = np.loadtxt(n, delimiter = ' ') #abrir archivo 1
    f2 = pd.DataFrame(data=F2, columns=['mm','hr','tn'])
    
    F00 = np.loadtxt(pathfromfill, delimiter = ' ') #abrir archivo 1
    F00 = pd.DataFrame(data=F00, columns=['mm','hr','tn'])
    
    #print(f2)
    
    DF2 = pd.concat([f2, F00], axis=1, ignore_index=True)
    #del DF2[5]
    #del DF2[1]
    #del DF2[3]
    
    #DF2.columns = ['mm', 'tn', 'hr']
        
    #DF2 = DF2.sort_values(by=['mm','hr'])
    
    #print(DF)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 13:47:49 2019

@author: leo
"""

import pandas as pd
import numpy as np
import glob
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

pfrom = '/home/leo/Documents/tesis/Tacubaya/*'

path2 = '/home/leo/Documents/tesis/Tacubaya.csv'#path archivos de salida

path3 = '/home/leo/Documents/tesis/Productos/Anios/Tacubaya.csv'


f1 =[]

for names in glob.glob(pfrom):

    pts1 = pd.read_csv(names, usecols=['Station','DateTime','Rh','ATC','SR','Rain','AvgWSU',
                                       'AvgWSV'], skiprows=[1])
    

    
    #df = df[['mean', '0', '1', '2', '3']]
    #'sr','pp','rh','tn','ws','wd'
    
    pts1 = pts1[['Station','DateTime','SR','Rain','Rh','ATC','AvgWSU','AvgWSV']]
    
    pts1['FechaTiempo'] = pts1['DateTime']
    #X =  pd.merge(pts1, Y)
    
    print(pts1)
    
    
    #pts1['Datetime'] = pd.to_datetime(pts1['Datetime'], format='%d/%m/%Y %I:%M:%S ')
    
    with open(path2, 'a') as f:
        
        #next(f)
        
        pts1.to_csv(f, header = False , sep = ' ',index=False, na_rep = np.nan)
        
    #with open(path3, 'a') as f1:
        
        #f1.write(year+',')
        #f1.write(names+',')
    
    #print(pts1)
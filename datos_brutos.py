s#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 19:06:39 2018

@author: leo
"""

import pandas as pd
import numpy as np
import glob
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

pfrom = '/home/leo/Documents/tesis/ESIME/Zacatecas/*'

path2 = '/home/leo/Documents/tesis/ESIMES_SALIDAS/Zacatecas.csv'#path archivos de salida

path3 = '/home/leo/Documents/tesis/Productos/Anios/Zacatecas.csv'
#pfrom = '/home/leo/Dropbox/Tesis/ESIME_Zacatecas/*'

#path2 = ('/home/leo/Dropbox/Tesis/zacatecas/')#path archivos de salida

#path3 = ('/home/leo/Dropbox/Tesis/zacatecas/zacatecastest.csv')


for names in glob.glob(pfrom):

    pts1 = pd.read_csv(names, usecols=['Estacion','Fecha-Tiempo','SR(W/m^2)','Rain(mm) 1Hr','RH %','ATC(C)',
                                       'WS(m/s)','WD'])
    
 
    pts1['Fecha-Tiempo'] = pts1['Fecha-Tiempo'].replace({'.m.' : 'm'}, regex=True)

    pts1['Datetime'] = pd.to_datetime(pts1['Fecha-Tiempo'], format='%d/%m/%Y %I:%M:%S %p')
     
    print(names)
    
    #x1,x2, year = names.split(' ')
    #x1,x2,year,x4 = names.split(' ')
    #year = year.replace('.csv','')
    
    #print(year)
    
    with open(path2, 'a') as f:
        
        pts1.to_csv(f, header = False , sep = ' ',index=False, na_rep = np.nan)
        
    with open(path3, 'a') as f1:
        
        #f1.write(year+',')
        f1.write(names+',')
    
        
    
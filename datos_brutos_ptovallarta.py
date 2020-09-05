#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 12:49:25 2019

@author: leo
"""

import pandas as pd
import numpy as np
import glob
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

pfrom = '/home/leo/Documents/tesis/Ptovallarta/*'

path2 = '/home/leo/Documents/tesis/ptovallarta'#path archivos de salida

#pfrom = '/home/leo/Dropbox/Tesis/ESIME_Zacatecas/*'

#path2 = ('/home/leo/Dropbox/Tesis/zacatecas/')#path archivos de salida

#path3 = ('/home/leo/Dropbox/Tesis/zacatecas/zacatecastest.csv')

f1 =[]

for names in glob.glob(pfrom):

    pts1 = pd.read_csv(names, skiprows=1, usecols=['Date','Time','Out','Speed','Dir','Rain',
                                       'Rad.'])
    
 
    #pts1['Fecha-Tiempo'] = pts1['Fecha-Tiempo'].replace({'.m.' : 'm'}, regex=True)

    #pts1['Datetime'] = pd.to_datetime(pts1['Fecha-Tiempo'], format='%d/%m/%Y %I:%M:%S %p')
     
    print(names)
    #print(pts1)
    
    with open(path2, 'a') as f:
        #writer.writerow(['ID', 'time1','rd','pp','rh','tt','ws','wd','time2'])
        pts1.to_csv(f, header = ('date','time','tt','ws','wd','pp','rad'), sep = ' ',index=False, na_rep = np.nan)
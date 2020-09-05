#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 01:06:35 2019

@author: leo
"""

import numpy as np
import glob
import pandas as pd
from pandas.compat import StringIO
import matplotlib.pyplot as plt
from astropy.table import Table, Column
import csv

epfrom = ('/home/leo/Documents/tesis/Productos/e/*')

p2 = '/home/leo/Documents/tesis/Productos/'

p3 = '/home/leo/Documents/tesis/Metadata/'

p7 = '/home/leo/Documents/tesis/Metadata/TOTALINDEX/INDEXSH.csv'


###############################################################################
######           Humedad Espcífica
###############################################################################


z = pd.read_excel('/home/leo/Documents/tesis/Estaciones Seleccionadas.xlsx')
    
Z = z['Altitud (msnm)']

    
z['Altitud (msnm)'] = 1008.4 - 0.102*z['Altitud (msnm)']
    

for l in glob.glob(epfrom):
    
    ee = pd.read_csv(l, header=None)
    
    #print(ee)

    shname0 = l.split('/')
    shname = shname0[7]
    shname = shname.replace('.csv','')
    
    #print(shname)
    
    for ll in z['Lugar']:
        if ll == shname:
            SH = 622*(ee/z['Altitud (msnm)'])
            SH = np.round(SH, decimals=1)
            
            VALSH=[]
            for j10 in SH[0]:
                if j10 > 17:
                    j10 = str(j10)
                    j10 = j10.replace(j10,'A')
                    #print (j4)
                elif j10 <= 17 and j10 > 12: 
                    j10 = str(j10)
                    j10 = j10.replace(j10,'M+')
                    #print (j4)
                elif j10 <= 12 and j10 > 7:
                    j10 = str(j10)
                    j10 = j10.replace(j10,'M-')
                    #print (j4)
                elif j10 <= 7:
                    j10 = str(j10)
                    j10 = j10.replace(j10,'B')
                    #print (j4)
                else:
                    break
    #print(j4)
                VALj10 = '{}'.format(j10)
                VALSH.append(VALj10)            
            
            print(VALj10)
            
            plt.plot([1,2,3,4,5,6,7,8,9,10,11,12],SH)

            plt.xlabel('Mes')
            plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])
            plt.xlim(1,12)
            plt.ylim(0,25)
            plt.ylabel('$gr/kg$')
            plt.grid(True, linestyle='--')
            plt.title('Humedad específica ' + str(ll))

            plotSH = '/'.join([p2,'Humedad_Especifica/plotSH' + str(shname) + '.png'])

            plt.savefig(plotSH)
            
            plt.show()
            
            with open(p7, 'a') as file18:
        
                SH[0].to_csv(file18, header = False , sep = ' ',index=False, na_rep = np.nan)
                
            pathindexdatash = ''.join([p2,'IndexdataSH/'+'ind_' + str(shname) + '.csv'])
    
            indexdatash = Table([DFPP['mm'],SH[0],VALSH],names=('mm','SH','VALSH'))
            #indexdatash = Table([DFPP['mm'],SH[0]],names=('mm','SH'))#,'VALSH'))
            print(indexdatash)
    
            with open(pathindexdatash, 'w') as csvfile2:
                writer = csv.writer(csvfile2)
                writer.writerow(['mm','SH','VALSH'])
                [writer.writerow(r) for r in indexdatash]
       
        else:
            ll.count(ll)
            
            

        
    print(SH)
        
    pathSH = ''.join([p3,'TOTALINDEX/'+ 'INDEXSH.csv'])
    
    with open(pathSH, 'a') as file18:
        
        SH[0].to_csv(file18, header = False , sep = ' ',index=False, na_rep = np.nan)
        
    #pathindexdatash = ''.join([p2,'IndexdataSH/'+'ind_' + str(estacion) + '.csv'])
    
    #indexdatash = Table([DFPP['mm'],SH,VALSH],names=('mm','SH','VALSH'))
    #print(indexdatash)
    
    #with open(pathindexdatash, 'w') as csvfile2:
    #    writer = csv.writer(csvfile2)
    #    writer.writerow(['mm','SH','VALSH'])
    #    [writer.writerow(r) for r in indexdatash]
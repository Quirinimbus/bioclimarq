#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 17:36:21 2019

@author: leo
"""

import numpy as np
import glob
import pandas as pd
from pandas.compat import StringIO
import matplotlib.pyplot as plt
from astropy.table import Table, Column
import csv

observadotemp = ('/home/leo/Documents/tesis/Productos/TempHoraria/Pto Vallarta.csv')

estimadotemp = ('/home/leo/Documents/tesis/Metadata/TEMPHORA_ESTIMADA/Pto Vallarta.csv')

observadohum = ('/home/leo/Documents/tesis/Productos/HumHoraria/Pto Vallarta.csv')

estimadohum = ('/home/leo/Documents/tesis/Metadata/HUMHORA_ESTIMADA/Pto Vallarta.csv')

scattertemp = ('/home/leo/Documents/tesis/Productos/ScatterTEMP/')

scatterhum = ('/home/leo/Documents/tesis/Productos/ScatterHUM/')

tempcorrrsme = '/home/leo/Documents/tesis/Productos/CORRRSME/corrrsmetemp.csv'

humcorrrsme = '/home/leo/Documents/tesis/Productos/CORRRSME/corrrsmehum.csv'

corrtemp = []

corrhum = []

for OBST in glob.glob(observadotemp):
    
    obst0 = np.loadtxt(OBST, delimiter = ' ') #abrir archivo 1
    obst = pd.DataFrame(data=obst0, columns=['mm','hr','tn'])
    
    #print(obst)
    
    OBST0 = OBST.split('/')
    obsTname = OBST0[7]
    obsTname = obsTname.replace('.csv', '')
    
    for ESTT in glob.glob(estimadotemp):
        ESTT0 = ESTT.split('/')
        estTname = ESTT0[7]
        estTname = estTname.replace('.csv', '')
            
        if estTname == obsTname:
            estt0 = np.loadtxt(ESTT, delimiter = ' ') #abrir archivo 1
            estt = pd.DataFrame(data=estt0, columns=['mm','hr','tn'])
            THORA = pd.merge(obst, estt,on = ['mm','hr'])
            
            #print(THORA)
            
            obstemp = THORA['tn_x']
            esttemp = THORA['tn_y']
            
            #print(obstemp)
            
            RSMET = (sum(obstemp - esttemp)/len(obstemp))**(1/2)
            RSMET = np.around(RSMET, decimals=2)
            
            rT = obstemp.corr(esttemp)
            rT = np.around(rT, decimals=2)
            
            plt.scatter(obstemp, esttemp, facecolor='red')
            plt.title('Temperatura ambiente horaria ' + obsTname)
            plt.xlabel('Observados')
            plt.ylabel('Estimados')
            
            
            plotSCATTERTEMP = '/'.join([scattertemp,'SCATEMP_' + str(estTname) + '.png'])    
    
            plt.savefig(plotSCATTERTEMP)
            
            plt.show()
            
            print(estTname)
            print(RSMET)
            print(rT)
            
            #str(rT)
            
            corrtemp = '{},{},{}\n'.format(estTname,rT,RSMET)
            #corrtemp = str(corrtemp)
            
            with open(tempcorrrsme, 'a') as f4:
                
                f4.write(corrtemp)
        
                #corrtemp.to_csv(f4 , sep = ' ',index=False, na_rep = np.nan)
            
            print(corrtemp)
            
            
            
for OBSH in glob.glob(observadohum):
    
    obsh0 = np.loadtxt(OBSH, delimiter = ' ') #abrir archivo 1
    obsh = pd.DataFrame(data=obsh0, columns=['mm','hr','rh'])
    
    #print(obsh)
    
    OBSH0 = OBSH.split('/')
    obsHname = OBSH0[7]
    obsHname = obsHname.replace('.csv', '')
    
    for ESTH in glob.glob(estimadohum):
        ESTH0 = ESTH.split('/')
        estHname = ESTH0[7]
        estHname = estHname.replace('.csv', '')
            
        if estHname == obsHname:
            esth0 = np.loadtxt(ESTH, delimiter = ' ') #abrir archivo 1
            esth = pd.DataFrame(data=esth0, columns=['mm','hr','rh'])
            HHORA = pd.merge(obsh, esth,on = ['mm','hr'])
            
            #print(HHORA)
            
            obshum = HHORA['rh_x']
            esthum = HHORA['rh_y']
            
            #print(obstemp)
            RSMEH = (sum(obshum - esthum)/len(obshum))**(1/2)
            RSMEH = np.around(RSMEH, decimals=5)
            
            #rH = np.corrcoef(obshum,esthum)
            rH = obshum.corr(esthum)
            rH = np.around(rH, decimals=2)
            
            plt.scatter(obshum, esthum, facecolor='green')
            plt.title('Humedad relativa horaria ' + obsHname)
            plt.xlabel('Observados')
            plt.ylabel('Estimados')
            
            
            plotSCATTERHUM = '/'.join([scatterhum,'SCAHUM_' + str(estHname) + '.png'])    

            plt.savefig(plotSCATTERHUM)
            
            plt.show()
            
            corrhum = '{},{},{}\n'.format(estHname,rH,RSMEH)
            #corrtemp = str(corrhum)
            
            print(corrhum)
            
            with open(humcorrrsme, 'a') as f5:
                
                f5.write(corrhum)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 18:45:14 2019

@author: leo
"""

import numpy as np
import glob
import pandas as pd
from pandas.compat import StringIO
import matplotlib.pyplot as plt
from astropy.table import Table, Column
import csv

#pfrom = ('/home/leo/Documents/tesis/Productos/Precip/*')

pfrom = ('/home/leo/Documents/tesis/Metadata/MetaPrecip/*')

p2 = '/home/leo/Documents/tesis/Productos/'

p4 = '/home/leo/Documents/tesis/Metadata/TOTALINDEX/INDEXOT1.csv'

p5 = '/home/leo/Documents/tesis/Metadata/TOTALINDEX/INDEXOT2.csv'

p6 = '/home/leo/Documents/tesis/Metadata/TOTALINDEX/PSUD.csv'

indexot1 = []


for entry in glob.glob(pfrom):
    
    #print(entry)
    
    estacion0 = entry.split('/')
    estacion = estacion0[7]
    estacion = estacion.replace('.csv', '')
    
    #print(estacion)

    DFPP = pd.read_csv(entry, header = None, sep =' ', names=['mm','pp','tn'])
    
    
###############################################################################
######           Índice Ombrotérmico
###############################################################################
    T = DFPP.tn
    PP = DFPP.pp
    
    ppmax = DFPP.max()

    OT1 = (PP/(2*T)) - 1 #Propuesta por Gómez Azpeitia
    
    print(DFPP)
    
    #print('OT1 =', len(OT1))

    fig, ax4 = plt.subplots()

    ax5 = ax4.twinx()
    ax4.plot(T, 'red')
    
    #ax5.plot(DFTN['mm'], PP, 'blue')
    ax4.set_xticks(DFPP['mm'])
    ax4.set_xlim(1,12)

    ax4.set_ylim(-1,((ppmax['pp']/2)))

    PP.plot(kind='bar', x='mm', y='pp', color = 'blue', ax=ax5, label='$PP$')

    ax4.set_xlabel('Mes')
    ax4.set_ylabel('Temp (°C)')
    ax4.set_title('Ombrotérmico ' + str(estacion))
    ax4.grid(True, linestyle='--')
    ax5.set_ylabel('mm')

    plotOH1 = '/'.join([p2,'Ombrotermico/plotOH1' + str(estacion) + '.png'])

    plt.savefig(plotOH1)
    
    plt.show()
    
    OT2 = PP/T # Propuesta por Enriqueta García
#print(OT1)

    OT1 = np.round(OT1, decimals=1)
    OT2 = np.round(OT2, decimals=1)

    VALOT1 = []

    for j1 in OT1:
        if j1 >= 0:
            j1 = str(j1)
            j1 = j1.replace(j1,'LL')
            #print (j)
        else:
            j1 = str(j1)
            j1 = j1.replace(j1,'D')

        VALj1 = '{}'.format(j1)
        VALOT1.append(VALj1)
        
        
        
        
###############################################################################
######           Precipitación suficiente para su uso doméstico
###############################################################################
    
    agua = (34.67,34.67,34.67,34.67,34.67,34.67,34.67,34.67,34.67,34.67,34.67,34.67)
    
    PSUD = (PP*10)/346.7
    
    PSUD = np.round(PSUD, decimals=1)
    
    #print(PSUD)
    
    
    fig, ax6 = plt.subplots()

    #ax7 = ax6.twinx()
    ax6.plot(agua, 'black', label='$PSUD$')
    
    #ax5.plot(DFTN['mm'], PP, 'blue')
    #ax6.set_xticks(DFTN['mm'], minor=False)
    ax6.set_xlim(1,12)

    #ax6.set_ylim(0,ppmax['pp'])

    DFPP.plot(kind='bar', x='mm', y='pp', color = 'blue', ax=ax6, label='$PP$')

    ax6.set_xlabel('Mes')
    ax6.set_ylabel('mm')
    ax6.set_title('PSUD ' + str(estacion))
    ax6.grid(True, linestyle='--')
    ax6.set_ylabel('mm')

    plotPSUD = ''.join([p2,'PSUD/PSUD' + str(estacion) + '.png'])
    
    #print(plotPSUD)

    plt.savefig(plotPSUD)
    
    plt.show()
    
    VALPSUD = []

    for j9 in PSUD:
        if j9 >= 1:
            j9 = str(j9)
            j9 = j9.replace(j9,'S')
            #print (j)
        else:
            j9 = str(j9)
            j9 = j9.replace(j9,'I')

        VALj9 = '{}'.format(j9)
        VALPSUD.append(VALj9)
    
    
###############################################################################
######           PRINT
###############################################################################
    #print('VALOT1=', len(VALOT1))
    
    #indexdata = str(indexdata)

    pathindexdatapp = ''.join([p2,'IndexdataPRECIP/'+'ind_' + str(estacion) + '.csv'])
    
    indexdatapp = Table([DFPP['mm'],OT1,VALOT1,OT2,PSUD,VALPSUD],
                      names=('mm','OT1','VALOT1','OT2','PSUD','VALPSUD'))
    print(indexdatapp)
    
    with open(pathindexdatapp, 'w') as csvfile1:
        writer = csv.writer(csvfile1)
        writer.writerow(['mm','OT1','VALOT1','OT2','PSUD','VALPSUD'])
        [writer.writerow(r) for r in indexdatapp]
        
       
    with open(p4, 'a') as file15:
        
        OT1.to_csv(file15, header = False , sep = ' ',index=False, na_rep = np.nan)
        
    with open(p5, 'a') as file16:
        
        OT2.to_csv(file16, header = False , sep = ' ',index=False, na_rep = np.nan)
    

    with open(p6, 'a') as file17:
        
        PSUD.to_csv(file17, header = False , sep = ' ',index=False, na_rep = np.nan)
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 18:16:46 2019

@author: leo
"""

import numpy as np
import glob
import pandas as pd
from pandas.compat import StringIO
import matplotlib.pyplot as plt
from astropy.table import Table, Column
import csv

pathindexes = ('/home/leo/Documents/tesis/Metadata/TOTALINDEX/*')

indexprintpath = ('/home/leo/Documents/tesis/Productos/METAINDEX/metaindex.csv')

plotprintpath = ('/home/leo/Documents/tesis/Productos/INDEXPLOT/')

pathchi2 = ('/home/leo/Documents/tesis/Productos/')

azpeitiaindex = []

for index in glob.glob(pathindexes):
    
    idx = pd.read_csv(index, header=None)
    
    #print(indexname,idx)
    
    meanidx = np.mean(idx)
    
    maxidx=np.max(idx)
    
    minidx=np.min(idx)
    
    #medianidx = np.median(idx)
    
    sig = np.std(idx)
    
    #ID = str(meanidx)
    
    #ID = ID.split(' ')
    #ID0 = ID[0]
    
    
    gx0 = (1/(sig*(2*np.pi)**(1/2)))*np.exp(-((1/2)*(idx - meanidx)**2/(sig)**2))

    dfgx0 = pd.DataFrame(gx0)
    dfidx = pd.DataFrame(idx)
    
    dfchi2 = pd.concat([dfidx,dfgx0],axis=1)
    
    dfchi2.columns = ['k1', 'k2']
    
    dfchi2 = np.round(dfchi2, decimals=1)
    
    dfchi2['kchi'] = ((dfchi2['k1'] - dfchi2['k2'])**2)/dfchi2['k2']
    
    chi2 = (dfchi2['kchi'].sum())
    
    chi2 = np.round(chi2, decimals=1)
    
    #names=['k1','k2']
    
    #print(dfgx0)
    
    indexname0 = index.split('/')
    indexname = indexname0[7]
    indexname = indexname.replace('.csv','')
    
    pathindexchi2 = ''.join([pathchi2,'chi2/'+'indchi2_' + str(indexname) + '.csv'])
    
        
    with open(pathindexchi2, 'w') as chi2x:
        
        chi2x.write(str(chi2))
    
    
    fig = plt.figure()
    plt.plot(idx, gx0, 'ro' )
    fig.suptitle(indexname, fontsize=20)

    if indexname == 'INDEXOT1':
        plt.xlabel(' ', fontsize=16)
        plt.axvline(x=0.0)
        
    elif indexname == 'INDEXOT2':
        plt.xlabel(' ', fontsize=16)
        plt.axvline(x=1.0)
        
    elif indexname == 'INDEXTH':
        plt.xlabel(' ', fontsize=16)
        plt.axvline(x=21.0)
        plt.axvline(x=16.0)

    elif indexname == 'INDEXHR':
        plt.xlabel('%', fontsize=16)
        plt.axvline(x=70.0)
        plt.axvline(x=50.0)
        plt.axvline(x=30.0)
        
    elif indexname == 'INDEXPSUD':
        plt.xlabel(' ', fontsize=16)
        plt.axvline(x=1.0)
        
    elif indexname == 'INDEXIT':
        plt.xlabel('°C', fontsize=16)
        plt.axvline(x=25.0)
        plt.axvline(x=20.0)
        plt.axvline(x=15.0)
        
    elif indexname == 'INDEXSR':
        plt.xlabel('$W \cdot m^{-2} \cdot dia$', fontsize=11)
        plt.axvline(x=7500.0)
        plt.axvline(x=5000.0)
        
    elif indexname == 'INDEXAH':
        plt.xlabel('$kg \cdot m^{-3}$', fontsize=11)
        plt.axvline(x=15.0)
        plt.axvline(x=10.0)
        plt.axvline(x=5.0)
        
    elif indexname == 'INDEXSH':
        plt.xlabel('$gr \cdot kg^{-1}$', fontsize=11)
        plt.axvline(x=17.0)
        plt.axvline(x=12.0)
        plt.axvline(x=7.0)


    plt.ylabel('', fontsize=16)
    
    plt.grid(True)
   
    plotINDEXGX = '/'.join([plotprintpath,'PLOTGX_' + str(indexname) + '.png'])

    plt.savefig(plotINDEXGX)
    
    plt.show()
    
    #x = [21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,37,18,49,50,100]
    #num_bins = 5
    #plt.hist(idx)
    #plt.show()
    
    (idx).hist(bins=10, normed = True, facecolor='green')    
    #idx.plot(kind='bar')
    plt.ylabel('Frecuencia', fontsize=16)
    
    
    
    if indexname == 'INDEXOT1':
        plt.xlabel(' ', fontsize=16)
        plt.axvline(x=0.0)
        
    elif indexname == 'INDEXOT2':
        plt.xlabel(' ', fontsize=16)
        plt.axvline(x=1.0)
        
    elif indexname == 'INDEXTH':
        plt.xlabel(' ', fontsize=16)
        plt.axvline(x=21.0)
        plt.axvline(x=16.0)

    elif indexname == 'INDEXHR':
        plt.xlabel('%', fontsize=16)
        plt.axvline(x=70.0)
        plt.axvline(x=50.0)
        plt.axvline(x=30.0)
        
    elif indexname == 'INDEXPSUD':
        plt.xlabel(' ', fontsize=16)
        plt.axvline(x=1.0)
        
    elif indexname == 'INDEXIT':
        plt.xlabel('°C', fontsize=16)
        plt.axvline(x=25.0)
        plt.axvline(x=20.0)
        plt.axvline(x=15.0)
        
    elif indexname == 'INDEXSR':
        plt.xlabel('$W \cdot m^{-2} \cdot dia$', fontsize=11)
        plt.axvline(x=7500.0)
        plt.axvline(x=5000.0)
        
    elif indexname == 'INDEXAH':
        plt.xlabel('$kg \cdot m^{-3}$', fontsize=11)
        plt.axvline(x=15.0)
        plt.axvline(x=10.0)
        plt.axvline(x=5.0)
        
    elif indexname == 'INDEXSH':
        plt.xlabel('$gr \cdot kg^{-1}$', fontsize=11)
        plt.axvline(x=17.0)
        plt.axvline(x=12.0)
        plt.axvline(x=7.0)

        
        
        
        
    #plt.xlabel('$\sigma$', fontsize=18)
    plt.title(indexname, fontsize=16)
    
    plotINDEXHIS = '/'.join([plotprintpath,'PLOTHIS_' + str(indexname) + '.png'])    
    
    plt.savefig(plotINDEXHIS)
    
    #
    
    
    plt.show()
    
    #print('Xmean = ', meanidx)
    #print(meanidx0)
    #print('Xmedian = ', medianidx)
    #print('Sigma = ', sig)
    
    
    idx0 = '{} {} {}'.format(indexname,meanidx, sig)
    
    idx0 = str(idx0)
    
    azpeitiaindex.append(idx0)
    
azpeitiaindex = '\n'.join(azpeitiaindex)
    
#azpeitiaidx='\n'.join(azpeitiaidx)
    
with open(indexprintpath, 'w') as AZIDX:
    #azpeitiaindex.to_csv(AZIDX, header = False , sep = ' ',index=False, na_rep = np.nan)
    AZIDX.write(str(azpeitiaindex))
    

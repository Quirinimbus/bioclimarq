#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 22:23:53 2019

@author: leo
"""

import numpy as np
import glob
import pandas as pd
from pandas.compat import StringIO
import matplotlib.pyplot as plt
from astropy.table import Table, Column
import csv

pfrom = ('/home/leo/Documents/tesis/ESIMES_SALIDAS/*')

p2 = '/home/leo/Documents/tesis/Productos/'

p3 = '/home/leo/Documents/tesis/Metadata/'


#################################################################################

################   ACOMODO DE BASE DE DATOS

################################################################################# 


for entry in glob.glob(pfrom):
    
    #print(entry)
    
    estacion0 = entry.split('/')
    estacion = estacion0[6]
    estacion = estacion.replace('.csv', '')

    file1 = (open(entry))
    next(file1)
    f0 = file1.readlines()
    file1.close
    f1 = []
    
    #print(file1)

    for i in range(len(f0)):
        
        tmpln = f0[i]
               
        ID, time0, x0, time = tmpln.split('"',3)
          
        time = time.replace('"','')
        
        time = time.replace('-',' ')
        
        time = time.replace('/',' ')
        
        time = time.replace(':',' ')
        
        time = time.replace('\n','')
        
        #print(time)
        
        tmpln0 = '{}{}'.format(time, x0)
                                
        f1.append(tmpln0)
    
    f1='\n'.join(f1)
        
    DF0 = pd.read_csv(StringIO(f1), sep=" ", header = None, error_bad_lines=False, low_memory=False,
                      names=['aa','mm','dd','hr','mn','se','sr','pp','rh','tn','ws','wd','xx'])
    
    del DF0['xx']
       
    DF0 = DF0.sort_values(by=['aa', 'mm', 'dd','hr','mn','se'])
            
    DF0 = DF0.fillna(-99.9)
       
    df = pd.DataFrame(DF0, columns=['aa','mm','dd','hr','mn','se','sr','pp','rh','tn','ws','wd'])
    
    #df = df[(df.aa > 2012) & (df.aa < 2017)]
    
    df = df.fillna(-99.9)
    
    df = df.apply(pd.to_numeric, errors = 'coerce')
    
    df = df.sort_values(by=['aa', 'mm', 'dd','hr','mn','se'])
    
    #print(df)
    
#################################################################################
################    TRABAJO CON VARIABLES !
#################################################################################

    df1 = df[(df.tn > -25.0) & (df.tn < 60)] # temperatura

    df2 = df[(df.sr > 0) & (df.sr < 1400)] # rad solar

    df3 = df[(df.rh > 4) & (df.rh < 101)] # hum relativa

    df4 = df[(df.pp >= 0) & (df.pp < 15)] # preciptación
    
###############################################################################
######           Radiación Solar
###############################################################################

    dfsr =  pd.DataFrame(data = df2, columns = ['aa', 'mm', 'dd','hr','mn','sr'])

    #dfsr['sr'] = (3.6)*dfsr['sr']
    
    #print (dfsr)

    srmensual1 = dfsr.groupby(['aa','mm','dd','hr'], as_index=False)['sr'].mean()
    srmensual1 = np.round(srmensual1, decimals=1)

    srmensual2 = srmensual1.groupby(['aa','mm','dd'], as_index=False)['sr'].sum()
    srmensual2 = np.round(srmensual2, decimals=1)
    
    #srmensual2 = srmensual2.groupby(['mm'], as_index=False)['sr'].sum()

    #print(srmensual2)

    srmensual = srmensual2.groupby(['mm'], as_index=False)['sr'].mean()
    srmensual = np.round(srmensual, decimals=1)
    
    
    plt.plot([1,2,3,4,5,6,7,8,9,10,11,12],srmensual['sr'], color = 'black')

    plt.xlabel('Mes')
    plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])
    plt.xlim(1,12)
    plt.ylim(2000,10000)
    plt.ylabel('$W /m^2 \cdot dia$')
    plt.grid(True, linestyle='--')
    plt.title('Radiación solar horizontal ' + str(estacion))

    plotSR = '/'.join([p2,'Radiacion/plotSR' + str(estacion) + '.png'])

    plt.savefig(plotSR)

    plt.show()
    #print(srmensual)
    
###############################################################################
######           Humedad Relativa
###############################################################################

    dfrh = pd.DataFrame(data = df3, columns = ['aa', 'mm', 'dd','hr','mn','rh'])

    rhmean = dfrh.groupby(['mm'], as_index=False)['rh'].mean()
    rhmean = np.round(rhmean, decimals=1)

    rhmeanhr = dfrh.groupby(['mm','dd','hr'], as_index=False)['rh'].mean()
    rhmax = rhmeanhr.groupby(['mm','dd'], as_index=False)['rh'].max()
    rhmaxmean = rhmax.groupby(['mm'], as_index=False)['rh'].mean()
    rhmaxmean = np.round(rhmaxmean, decimals=1)

    rhmeanhr = dfrh.groupby(['mm','dd','hr'], as_index=False)['rh'].mean()
    rhmin = rhmeanhr.groupby(['mm','dd'], as_index=False)['rh'].min()
    rhminmean = rhmin.groupby(['mm'], as_index=False)['rh'].mean()
    rhminmean = np.round(rhminmean, decimals=1)

    #print (rhminmean)

    RH0 = pd.merge(rhminmean, rhmaxmean,on = ['mm'])
    
    
    
    #RH0.to_csv(HumMaxMin, index=False, header = False, sep = ' ')
    
    #print(RH0)

    RH = pd.merge(RH0, rhmean, on = ['mm'])#, columns = ['rhmax','rhmin','rh'])

    #print(RH)

    rhhora = dfrh.groupby(['mm','hr'], as_index=False)['rh'].mean()
    rhhora = np.round(rhhora, decimals=0)
    
    HumHora = '/'.join([p2,'HumHoraria/' + str(estacion) + '.csv'])
    
    rhhora.to_csv(HumHora, index=False, header = False, sep = ' ')
    
    ax1 = plt.gca()
    ax1.set_xticks(RH['mm'])
    ax1.set_xlim(1,12)
    ax1.set_ylim(0,100)

    #plt.boxplot(RH)
    
    RH.plot(kind='line',x='mm', y='rh_x', color = 'green', ax=ax1, label='$RH_{max}$')
    RH.plot(kind='line',x='mm', y='rh', color = 'black', ax=ax1, label='$RH$')
    RH.plot(kind='line',x='mm',y='rh_y', color='green', ax=ax1, label='$RH_{min}$')
    
    plt.fill_between(RH['mm'],RH['rh_y'],RH['rh_x'], facecolor='green', alpha=0.2)
    ax1.set_xlabel('Mes')
    ax1.set_ylabel('Humedad (%)')
    ax1.set_title('Humedad relativa promedio ' + str(estacion))
    ax1.grid(True, linestyle='--')

    plotrh = '/'.join([p2,'Humedad/plotrh' + str(estacion) + '.png'])

    plt.savefig(plotrh)

    plt.show()
    
    
###############################################################################
######           Temperatura Ambiente
###############################################################################

    dftn = pd.DataFrame(data = df1, columns = ['aa', 'mm', 'dd','hr','mn','tn'])
    dftn = dftn[np.abs(dftn.tn-dftn.tn.mean())<=(3*dftn.tn.std())] # Elimina valores > |3 desviaciones estándares| 
        
    tnmean = dftn.groupby(['mm'], as_index=False)['tn'].mean()
    tnmean = np.round(tnmean, decimals=1)

    tnmax = dftn.groupby(['aa','mm','dd'], as_index=False)['tn'].max()
    tnmaxmean = tnmax.groupby(['mm'], as_index=False)['tn'].mean()
    tnmaxmean = np.round(tnmaxmean, decimals=1)

    tnmin = dftn.groupby(['aa','mm','dd'], as_index=False)['tn'].min()
    tnminmean = tnmin.groupby(['mm'], as_index=False)['tn'].mean()
    tnminmean = np.round(tnminmean, decimals=1)

    tnhora = dftn.groupby(['mm','hr'], as_index=False)['tn'].mean()
    tnhora = np.round(tnhora, decimals=1)
    
    Temp = '/'.join([p3,'MetaTemp/' + str(estacion) + '.csv'])
    
    tnmean.to_csv(Temp, index=False, header = False, sep = ' ')
    
    #print(tnhora)
    
    TempHora = '/'.join([p2,'TempHoraria/' + str(estacion) + '.csv'])
    
    tnhora.to_csv(TempHora, index=False, header = False, sep = ' ')

    TN =  pd.merge(tnmaxmean, tnminmean, on = ['mm'])
    
    TNMaxMin = '/'.join([p2,'TNMaxMin/' + str(estacion) + '.csv'])
    
    TN.to_csv(TNMaxMin, index=False, header = False, sep = ' ')

    Y0 =  pd.merge(RH, TN, on = ['mm']) 

    Y =  pd.merge(Y0, tnmean, on = ['mm'])
    #print (Y)

    DFTN = pd.merge(tnmean, TN, on = ['mm'])

    #DFTN = DFTN.pivot_table(index='mm', values=['tn_x','tn','tn_y'])

    print (DFTN)
    ax2 = plt.gca()
    ax2.set_xticks(DFTN['mm'], minor=False)
    ax2.set_xlim(1,12)
    ax2.set_ylim(0,45)

    #print(DFTN)
    
    DFTN.plot(kind='line',x='mm', y='tn_x', color = 'red', ax=ax2, label='$T_{max}$')
    DFTN.plot(kind='line',x='mm', y='tn', color = 'black', ax=ax2, label='$T$')
    DFTN.plot(kind='line',x='mm',y='tn_y', color='blue', ax=ax2, label='$T_{min}$')

    plt.fill_between(DFTN['mm'],DFTN['tn_y'],DFTN['tn_x'], facecolor='silver', alpha=0.6)
    ax2.set_xlabel('Mes')
    ax2.set_ylabel('Temp (°C)')
    ax2.set_title('Temperatura promedio ' + str(estacion))
    ax2.grid(True, linestyle='--')

    #plt.show()

    plotT = '/'.join([p2,'Temperatura/plotT' + str(estacion) + '.png'])

    plt.savefig(plotT)

    plt.show()
    
###############################################################################
######           Precipitación
###############################################################################

    dfpp = pd.DataFrame(data = df4, columns = ['aa', 'mm', 'dd','hr','mn','pp'])

    ppmeanhr =  dfpp.groupby(['aa','mm','dd','hr','mn'], as_index=False)['pp'].mean()
    ppmeanhr = np.round(ppmeanhr, decimals=1)
    
    df5 = ppmeanhr[(ppmeanhr.pp > 0) & (ppmeanhr.pp < 100)]
    
    ppaasum = df5.groupby(['aa','mm'], as_index=False)['pp'].sum()
    ppaasum = np.round(ppaasum, decimals=1)
    
    #print(ppaasum)
    
    ppmean = ppaasum.groupby(['mm'], as_index=False)['pp'].mean()
    ppmean = np.round(ppmean, decimals=1)
    
    PP0 =  pd.merge(ppmean, tnmean ,on = ['mm'])
    
    #how = 'outer'
    
    print(PP0)
    
    Precip = '/'.join([p2,'Precip/' + str(estacion) + '.csv'])
    
    PP0.to_csv(Precip, index=False, header = False, sep = ' ')
   
    ppmax = ppmean.max()
    
    #print(ppmean)
###############################################################################
######           Humedad de Saturación y Saturación
###############################################################################

    T = tnmean.tn #Temp. para ec.
    
    #print('T =', len(T))
    
    rh0 = rhmean.rh #Humedad para ec.
    
    #print('rh0 =', len(rh0))

    es = 6.63 + 0.458*T + 4.6 * 10**(-3) * (T)**2 + 6.6 * 10**(-4) * (T)**3 
    
    #print('es =', len(es))
    
    e = es * (rh0)/100

    es = np.round(es, decimals=1)
    e = np.round(e, decimals=1)
    
    edata = '/'.join([p2,'e/' + str(estacion) + '.csv'])
    
    e.to_csv(edata, index=False, header = False, sep = ' ')
    
    #print(e)
    
###############################################################################
######           Humedad Abosulta
###############################################################################

    AH = 217*(e/(T + 273.15))
    AH = np.round(AH, decimals=1)
    
    #print('AH =', len(AH))
    #print(AH)

    plt.plot([1,2,3,4,5,6,7,8,9,10,11,12],AH)

    plt.xlabel('Mes')
    plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])
    plt.xlim(1,12)
    plt.ylim(0,30)
    plt.ylabel('$gr/m^3$')
    plt.grid(True, linestyle='--')
    plt.title('Humedad absoluta ' + str(estacion))

    plotAH = '/'.join([p2,'Humedad_Absoluta/plotAH' + str(estacion) + '.png'])

    plt.savefig(plotAH)

    plt.show()
    
###############################################################################
######           Humedad Espcífica
###############################################################################
    
    z = pd.read_excel('/home/leo/Documents/tesis/Estaciones Seleccionadas.xlsx')
    
    Z = z['Altitud (msnm)']
    
    P = 1008.4 - 0.102*Z #presión
    
    #print(P)
    
    Presion = '/'.join([p2,'Presion/' + str(estacion) + '.csv'])
    
    P.to_csv(Presion, index=False, header = False, sep = ' ')
   
###############################################################################
######           Índice Termohidríco
###############################################################################

    TH1 = (T + AH)*(1/2) #Propuesta por Gómez Azpeitia
    
    #print('TH1 =', len(TH1))
    
    TH1 = np.round(TH1, decimals=1)
    #print(TH1)

    plt.plot([1,2,3,4,5,6,7,8,9,10,11,12],TH1)

    plt.xlabel('Mes')
    plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])
    plt.xlim(1,12)
    plt.ylim(0,30)
    plt.ylabel('')
    plt.grid(True, linestyle='--')
    plt.title('Termohígrico ' + str(estacion))

    plotTH = '/'.join([p2,'Termohigrico/plotTH' + str(estacion) + '.png'])

    plt.savefig(plotTH)

    plt.show()

    VALTH1 = []
    for j2 in TH1:
        if j2 > 21:
            j2 = str(j2)
            j2 = j2.replace(j2,'A')
        #print (j2)
        elif j2 <= 21 and j2 > 15.8: 
            j2 = str(j2)
            j2 = j2.replace(j2,'M')
        #print (j2)
        elif j2 <= 15.8 and j2 > 4:
            j2 = str(j2)
            j2 = j2.replace(j2,'B')
            #print (j2)
        else:
            break
        VALj2 = '{}'.format(j2)
        VALTH1.append(VALj2)
        
    pathTH = ''.join([p3,'TOTALINDEX/'+ 'INDEXTH.csv'])
    with open(pathTH, 'a') as file10:
        
        TH1.to_csv(file10, header = False , sep = ' ',index=False, na_rep = np.nan)

    #print('VALTH1=', len(VALTH1))
    
###############################################################################
######           Índice Térmico
###############################################################################


    VALT = []
    for j3 in T:
    
        if j3 > 25:
            j3 = str(j3)
            j3 = j3.replace(j3,'K')
            #print (j3)
        elif j3 <= 25 and j3 > 20: 
            j3 = str(j3)
            j3 = j3.replace(j3,'C')
        #print (j3)
        elif j3 <= 20 and j3 > 15:
            j3 = str(j3)
            j3 = j3.replace(j3,'T')
        #print (j3)
        elif j3 <= 15:
            j3 = str(j3)
            j3 = j3.replace(j3,'F')
        #print (j3)
        else:
            break
    #print(j3)
    #VALT = ''j3
        VALj3 = '{}'.format(j3)
        VALT.append(VALj3)
        
    pathIT = ''.join([p3,'TOTALINDEX/'+ 'INDEXIT.csv'])
    with open(pathIT, 'a') as file11:
        
        T.to_csv(file11, header = False , sep = ' ',index=False, na_rep = np.nan)
    #print('VALT=', len(VALT))
        
        
###############################################################################
######           Índice Humedad Relativa
###############################################################################
        
        
    VALrh0=[]
    for j4 in rh0:
        if j4 > 70:
            j4 = str(j4)
            j4 = j4.replace(j4,'H')
            #print (j4)
        elif j4 <= 70 and j4 > 50: 
            j4 = str(j4)
            j4 = j4.replace(j4,'SH')
            #print (j4)
        elif j4 <= 50 and j4 > 30:
            j4 = str(j4)
            j4 = j4.replace(j4,'SS')
                        #print (j4)
        elif j4 <= 30:
            j4 = str(j4)
            j4 = j4.replace(j4,'A')
            #print (j4)
        else:
            break
    #print(j4)
        VALj4 = '{}'.format(j4)
        VALrh0.append(VALj4)
    #print('VALrh0=', len(VALrh0))
#VALrh0 = '\n'.join(VALrh0)
    
    pathHR = ''.join([p3,'TOTALINDEX/'+ 'INDEXHR.csv'])
    with open(pathHR, 'a') as file12:
        
        rh0.to_csv(file12, header = False , sep = ' ',index=False, na_rep = np.nan)

#print(VALrh0)
        
###############################################################################
######           Índice Humedad Absoluta
###############################################################################

    VALAH=[]
    for j5 in AH:
        if j5 > 15:
            j5 = str(j5)
            j5 = j5.replace(j5,'A')
        #print (j4)
        elif j5 <= 15 and j5 > 10: 
            j5 = str(j5)
            j5 = j5.replace(j5,'M+')
            #print (j4)
        elif j5 <= 10 and j5 > 5:
            j5 = str(j5)
            j5 = j5.replace(j5,'M-')
        #print (j4)
        elif j5 <= 5:
            j5 = str(j5)
            j5 = j5.replace(j5,'B')
        #print (j4)
        else:
            break
    #print(j4)
        VALj5 = '{}'.format(j5)
        VALAH.append(VALj5)
        
    pathAH = ''.join([p3,'TOTALINDEX/'+ 'INDEXAH.csv'])
    with open(pathAH, 'a') as file13:
        
        AH.to_csv(file13, header = False , sep = ' ',index=False, na_rep = np.nan)
    #print(VALAH, len(VALAH))
#VALAH = '\n'.join(VALAH)

#print(VALAH)
    
###############################################################################
######           Índice Radiación
###############################################################################
        
    SR = srmensual.sr

    VALSR=[]

    for j5 in SR:
        if j5 > 7500:
            j5 = str(j5)
            j5 = j5.replace(j5,'I')
            #print (j5)
        elif j5 <= 7500 and j5 > 5000: 
            j5 = str(j5)
            j5 = j5.replace(j5,'M')
        #print (j5)
        elif j5 <= 5000:
            j5 = str(j5)
            j5 = j5.replace(j5,'D')
        #print (j5)
        else:
            break
        VALj5 = '{}'.format(j5)
        VALSR.append(VALj5)
        
    pathSR = ''.join([p3,'TOTALINDEX/'+ 'INDEXSR.csv'])
    with open(pathSR, 'a') as file14:
        
        SR.to_csv(file14, header = False , sep = ' ',index=False, na_rep = np.nan)
    
    #print(VALSR, len(VALSR))
    
###############################################################################
######           Sección de Impresión
###############################################################################
    
    #printdata = data.tranpose()
    
    #print(printdata)

    #indexdata = Table(PP)
    
    #print(indexdata)

    indexdata = Table([tnmean['mm'],e,es,T,VALT,rh0,VALrh0,SR,VALSR,AH,VALAH,TH1,VALTH1],
                      names=('mm','e', 'es','T','INT','RH','INRH','SR','INSR','AH','INAH','TH1','INTH1'))
    #print(indexdata)

    #indexdata = str(indexdata)

    pathindexdata = ''.join([p2,'IndexdataTEMP/'+'ind_' + str(estacion) + '.csv'])
    
    #indexdata.to_csv(pathindexdata, index=False)
    
    #indexdata0 = Table([ppmean['mm'],PP,OT2,OT1,VALOT1],
                      #names=('mm','PP','OT2','OT1','VALOT1'))
    
    #printindexdata0 = '/'.join([p2,'IndexdataLLUVIA/'+'ind_' + str(estacion) + '.csv'])

    with open(pathindexdata, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['mm','e', 'es','T','INT','RH','INRH','SR','INSR','AH','INAH','TH1','INTH1'])
        [writer.writerow(r) for r in indexdata]

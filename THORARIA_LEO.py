# -*- coding: utf-8 -*-
"""
Created on Fri May 24 18:25:45 2019

@author: GUZZFERZ
"""

###############################################################################
###############################################################################
###   Programa desarrollado para el GCA de la Universidad Veracruzana
###   Realizado a partir del articulo:
###   "A comparative simple method for human bioclimatic conditions applied to  
###    seasonally hot/warm cities of Mexico"
###   A. TEJEDA-MARTINEZ y O. R. GARCIA-CUETO
###   Atmósfera #15 (2002), pp. 55-66
###############################################################################
###############################################################################

import numpy as np
import pandas as pd

pathtemphora = ('/home/leo/Documents/tesis/Metadata/TEMPHORA_ESTIMADA/Pto Vallarta.csv')

pathhumhora = ('/home/leo/Documents/tesis/Metadata/HUMHORA_ESTIMADA/Pto Vallarta.csv')

###############################################################################
###############################################################################
######          1.-  Entrada de datos 
###############################################################################
###############################################################################

####### escribir resultados directamente a un archivo de texto #######
#import sys
#sys.stdout = open('output.txt','wt')

#Loc = int(input('Ingrese la Localidad: '))
#Lat = int(input('Ingrese la latitud: '))


while True:
    try:
        Lat = 20.70
        #Lat = input('Ingrese la latitud: ')
        if Lat < -90 or Lat > 90:
            raise ValueError #this will send it to the print message and back to the input option
        break
    except ValueError:
        print("Valor invalido. El valor debe estar dentro de un rango de -90 a 90.")

#Lon = int(input('Ingrese la longitud: '))
while True:
    try:
        Lon = -105.22
        #Lon = input('Ingrese la longitud: ')
        if Lon < -180 or Lon > 180:
            raise ValueError #this will send it to the print message and back to the input option
        break
    except ValueError:
        print("Valor invalido. El valor debe estar dentro de un rango de -180 a 180.")

Alt = 20.0

#Alt = int(input('Ingrese la altitud: '))
#pres = int(input('Ingrese la presion: '))
DatHR = int(input('¿Cuentas con datos de humedad? (0=si, 1=no) '))
#DatHR = 1
#1print('Localidad =', Loc)
print('Latitud =', Lat)
print('Longitud =', Lon)
print('Altitud =', Alt)
#print'Presion (hPa) =', pres

print('Ingrese las Temperaturas maximas mensuales')
#Tmax2 = np.array([int(input('Enero:')), int(input('Febrero:')), int(input('Marzo:')), int(input('Abril:')), int(input('Mayo:')), int(input('Junio:')), int(input('Julio:')), int(input('Agosto:')), int(input('Septiembre:')), int(input('Octubre:')), int(input('Noviembre:')), int(input('Diciembre:'))])
Tmax2 = np.array([27.3,27.2,27.7,28.4,30.1,31.5,32.4,32.5,32,31.9,30.2,27.9])
Tmax = np.around(Tmax2, decimals=1)
print(Tmax)

print('Ingrese las Temperaturas minimas mensuales')
#Tmin2 = np.array([int(input('Enero:')), int(input('Febrero:')), int(input('Marzo:')), int(input('Abril:')), int(input('Mayo:')), int(input('Junio:')), int(input('Julio:')), int(input('Agosto:')), int(input('Septiembre:')), int(input('Octubre:')), int(input('Noviembre:')), int(input('Diciembre:'))])
Tmin2 = np.array([17.2,17.5,17.9,19.5,22.4,24.9,24.6,24.6,24.5,24.1,21.2,18.5])
Tmin = np.around(Tmin2, decimals=1)
print(Tmin)

print('Temperaturas medias mensuales')
Tmed2 = (Tmax + Tmin)/2
Tmed = np.around(Tmed2, decimals=1)
print(Tmed)

print('Hora min mensual')
Hrmin = np.array([12-(180*np.arccos(0.3896*np.tan(Lat*np.pi/180))/np.pi)/15, 12-(180*np.arccos(0.2368*np.tan(Lat*np.pi/180))/np.pi)/15, 12-(180*np.arccos(0.05*np.tan(Lat*np.pi/180))/np.pi)/15, 12-(180*np.arccos(-0.165*np.tan(Lat*np.pi/180))/np.pi)/15, 12-(180*np.arccos(-0.3397*np.tan(Lat*np.pi/180))/np.pi)/15, 12-(180*np.arccos(-0.4308*np.tan(Lat*np.pi/180))/np.pi)/15, 12-(180*np.arccos(-0.3947*np.tan(Lat*np.pi/180))/np.pi)/15, 12-(180*np.arccos(-0.2463*np.tan(Lat*np.pi/180))/np.pi)/15, 12-(180*np.arccos(-0.0399*np.tan(Lat*np.pi/180))/np.pi)/15, 12-(180*np.arccos(0.168*np.tan(Lat*np.pi/180))/np.pi)/15, 12-(180*np.arccos(0.3464*np.tan(Lat*np.pi/180))/np.pi)/15, 12-(180*np.arccos(0.4312*np.tan(Lat*np.pi/180))/np.pi)/15])
Hrmin2 = np.around(Hrmin, decimals=2)
print(Hrmin2)

print('Hora max mensual')
o = np.array([7.63, 9.5, 8.25, 9.38, 8.88, 9.25, 10.25, 10, 10.13, 9.68, 9.37, 8.75])
p =np.array([7.41, 7.5, 6.83, 7.67, 7.59, 7.91, 7.25, 7.5, 7.59, 7.17, 7.5, 7.25])
if Lat>=23.5 :
    hrm = Hrmin + o
else:
    hrm = Hrmin + p
Hrmax2 = np.around(hrm, decimals=2)
print(Hrmax2)

print('HR media calculada mensual')
if DatHR<=0 :
    HRmed = np.array([int(input('Enero:')), int(input('Febrero:')), int(input('Marzo:')), int(input('Abril:')), int(input('Mayo:')), int(input('Junio:')), int(input('Julio:')), int(input('Agosto:')), int(input('Septiembre:')), int(input('Octubre:')), int(input('Noviembre:')), int(input('Diciembre:'))])
else:
    HRmed = ((7.517268+0.084757*Tmin+0.03727*(Tmin**2)-0.001755*(Tmin**3)+0.000193*(Tmin**4)-0.000005*(Tmin**5))/(6.115+0.42915*Tmed+1.4206*(10**-2)*(Tmed**2)+3.046*(10**-4)*(Tmed**3)+3.2*(10**-6)*(Tmed**4)))*100
HRmed2 = np.around(HRmed, decimals=0)
print(HRmed2)

print('HR maxima calculada mensual')
if DatHR<=0 :
    HRmax = np.array([int(input('Enero:')), int(input('Febrero:')), int(input('Marzo:')), int(input('Abril:')), int(input('Mayo:')), int(input('Junio:')), int(input('Julio:')), int(input('Agosto:')), int(input('Septiembre:')), int(input('Octubre:')), int(input('Noviembre:')), int(input('Diciembre:'))])
else:
    if np.any((2*HRmed-(((HRmed/100)*(6.115+0.42915*Tmed+1.4206*(10**-2)*(Tmed**2)+3.046*(10**-4)*(Tmed**3)+3.2*(10**-6)*(Tmed**4)))/(6.115+0.42915*Tmax+1.4206*(10**-2)*(Tmax**2)+3.046*(10**-4)*(Tmax**3)+3.2*(10**-6)*(Tmax**4)))*100))>100 :
        HRmax = 100
    else:
        HRmax = 2*HRmed-(((HRmed/100)*(6.115+0.42915*Tmed+1.4206*(10**-2)*(Tmed**2)+3.046*(10**-4)*(Tmed**3)+3.2*(10**-6)*(Tmed**4)))/(6.115+0.42915*Tmax+1.4206*(10**-2)*(Tmax**2)+3.046*(10**-4)*(Tmax**3)+3.2*(10**-6)*(Tmax**4)))*100
HRmax2 = np.around(HRmax, decimals=0)
print(HRmax2)


print('HR minima calculada mensual')
if DatHR<=0 :
    HRmin = np.array([int(input('Enero:')), int(input('Febrero:')), int(input('Marzo:')), int(input('Abril:')), int(input('Mayo:')), int(input('Junio:')), int(input('Julio:')), int(input('Agosto:')), int(input('Septiembre:')), int(input('Octubre:')), int(input('Noviembre:')), int(input('Diciembre:'))])
else:
    if np.any((2*HRmed-(((HRmed/100)*(6.115+0.42915*Tmed+1.4206*(10**-2)*(Tmed**2)+3.046*(10**-4)*(Tmed**3)+3.2*(10**-6)*(Tmed**4)))/(6.115+0.42915*Tmax+1.4206*(10**-2)*(Tmax**2)+3.046*(10**-4)*(Tmax**3)+3.2*(10**-6)*(Tmax**4)))*100))>100 :
        HRmin = 2*HRmed-100
    else:
        HRmin = ((((HRmed/100)*(6.115+0.42915*Tmed+1.4206*(10**-2)*(Tmed**2)+3.046*(10**-4)*(Tmed**3)+3.2*(10**-6)*(Tmed**4)))/(6.115+0.42915*Tmax+1.4206*(10**-2)*(Tmax**2)+3.046*(10**-4)*(Tmax**3)+3.2*(10**-6)*(Tmax**4)))*100)
HRmin2 = np.around(HRmin, decimals=0)
print(HRmin2)
#hablar con el Dr para saber si se usa la Tmed o la Tmax
print('Presion de vapor de saturacion media mensual')
Es = (0.00066*(Tmed**3))+(0.0046*(Tmed**2))+(0.458*Tmed)+6.63
Es2 = np.around(Es, decimals=1)
print(Es2)

###############################################################################
###############################################################################
######          2.-  Temperatura Horaria
###############################################################################
###############################################################################

print('Temperatura horaria mensual')

n = np.array([[0], [1], [2], [3], [4], [5], [6], [7]]) 
m = np.array([[7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20], [21], [22], [23]])

#enero, febrero, noviembre y diciembre de 00:00 a 06:00
if Lat>=23.5 :
   if np.all(n)>=np.any(Hrmin) :
      Tefnd0006 = Tmin+(0.023*(n-Hrmin)**3.436)*(np.exp(-0.421*(n-Hrmin)))*(Tmax-Tmin)
   else:
      Tefnd0006 = Tmin+(0.023*(n+24-Hrmin)**3.436)*(np.exp(-0.421*(n+24-Hrmin)))*(Tmax-Tmin)
else:   
   if np.all(n)>=np.any(Hrmin) :
      Tefnd0006 = Tmin+(0.096*(n-Hrmin)**2.422)*(np.exp(-0.339*(n-Hrmin)))*(Tmax-Tmin)
   else:
      Tefnd0006 = Tmin+(0.096*(n+24-Hrmin)**2.422)*(np.exp(-0.339*(n+24-Hrmin)))*(Tmax-Tmin)

#enero, febrero, noviembre y diciembre de 07:00 a 23:00
if Lat>=23.5 :
   if np.any(n)>=np.all(Hrmin) :
      Tefnd0723 = Tmin+(0.023*(m-Hrmin)**3.436)*(np.exp(-0.421*(m-Hrmin)))*(Tmax-Tmin)
   else:
      Tefnd0723 = Tmin+(0.023*(m+24-Hrmin)**3.436)*(np.exp(-0.421*(m+24-Hrmin)))*(Tmax-Tmin)
else:   
   if np.any(n)>=np.all(Hrmin) :
      Tefnd0723 = Tmin+(0.096*(m-Hrmin)**2.422)*(np.exp(-0.339*(m-Hrmin)))*(Tmax-Tmin)
   else:
      Tefnd0723 = Tmin+(0.096*(m+24-Hrmin)**2.422)*(np.exp(-0.339*(m+24-Hrmin)))*(Tmax-Tmin)

#marzo, abril, mayo, junio, julio, agosto, 
#septiembre, octubre de 00:00 a 06:00
if Lat>=23.5 :
   if np.all(n)>=np.any(Hrmin) :
      Tmmjs0006 = Tmin+(0.026*(n-Hrmin)**3.19)*(np.exp(-0.375*(n-Hrmin)))*(Tmax-Tmin)
   else:
      Tmmjs0006 = Tmin+(0.026*(n+24-Hrmin)**3.19)*(np.exp(-0.375*(n+24-Hrmin)))*(Tmax-Tmin)
else:
   if np.all(n)>=np.any(Hrmin) :
      Tmmjs0006 = Tmin+(0.096*(n-Hrmin)**2.422)*(np.exp(-0.339*(n-Hrmin)))*(Tmax-Tmin)
   else:
      Tmmjs0006 = Tmin+(0.096*(n+24-Hrmin)**2.422)*(np.exp(-0.339*(n+24-Hrmin)))*(Tmax-Tmin)      
      
#marzo, abril, mayo, junio, julio, agosto, 
#septiembre, octubre de 00:07 a 23:00
if Lat>=23.5 :
   if np.any(n)>=np.all(Hrmin) :
      Tmmjs0723 = Tmin+(0.026*(m-Hrmin)**3.19)*(np.exp(-0.375*(m-Hrmin)))*(Tmax-Tmin)
   else:
      Tmmjs0723 = Tmin+(0.026*(m+24-Hrmin)**3.19)*(np.exp(-0.375*(m+24-Hrmin)))*(Tmax-Tmin)
else:
   if np.any(n)>=np.all(Hrmin) :
      Tmmjs0723 = Tmin+(0.096*(m-Hrmin)**2.422)*(np.exp(-0.339*(m-Hrmin)))*(Tmax-Tmin)
   else:
      Tmmjs0723 = Tmin+(0.096*(m+24-Hrmin)**2.422)*(np.exp(-0.339*(m+24-Hrmin)))*(Tmax-Tmin)

TEMHOR = np.array([[Tefnd0006[0][0], Tefnd0006[0][1], Tmmjs0006[0][2], Tmmjs0006[0][3], Tmmjs0006[0][4], Tmmjs0006[0][5], Tmmjs0006[0][6], Tmmjs0006[0][7], Tmmjs0006[0][8], Tmmjs0006[0][9], Tefnd0006[0][10], Tefnd0006[0][11]],
                   [Tefnd0006[1][0], Tefnd0006[1][1], Tmmjs0006[1][2], Tmmjs0006[1][3], Tmmjs0006[1][4], Tmmjs0006[1][5], Tmmjs0006[1][6], Tmmjs0006[1][7], Tmmjs0006[1][8], Tmmjs0006[1][9], Tefnd0006[1][10], Tefnd0006[1][11]],
                   [Tefnd0006[2][0], Tefnd0006[2][1], Tmmjs0006[2][2], Tmmjs0006[2][3], Tmmjs0006[2][4], Tmmjs0006[2][5], Tmmjs0006[2][6], Tmmjs0006[2][7], Tmmjs0006[2][8], Tmmjs0006[2][9], Tefnd0006[2][10], Tefnd0006[2][11]],
                   [Tefnd0006[3][0], Tefnd0006[3][1], Tmmjs0006[3][2], Tmmjs0006[3][3], Tmmjs0006[3][4], Tmmjs0006[3][5], Tmmjs0006[3][6], Tmmjs0006[3][7], Tmmjs0006[3][8], Tmmjs0006[3][9], Tefnd0006[3][10], Tefnd0006[3][11]],
                   [Tefnd0006[4][0], Tefnd0006[4][1], Tmmjs0006[4][2], Tmmjs0006[4][3], Tmmjs0006[4][4], Tmmjs0006[4][5], Tmmjs0006[4][6], Tmmjs0006[4][7], Tmmjs0006[4][8], Tmmjs0006[4][9], Tefnd0006[4][10], Tefnd0006[4][11]],
                   [Tefnd0006[5][0], Tefnd0006[5][1], Tmmjs0006[5][2], Tmmjs0006[5][3], Tmmjs0006[5][4], Tmmjs0006[5][5], Tmmjs0006[5][6], Tmmjs0006[5][7], Tmmjs0006[5][8], Tmmjs0006[5][9], Tefnd0006[5][10], Tefnd0006[5][11]],
                   [Tefnd0006[6][0], Tefnd0006[6][1], Tmmjs0006[6][2], Tmmjs0006[6][3], Tmmjs0006[6][4], Tmmjs0006[6][5], Tmmjs0006[6][6], Tmmjs0006[6][7], Tmmjs0006[6][8], Tmmjs0006[6][9], Tefnd0006[6][10], Tefnd0006[6][11]],
                   [Tefnd0723[0][0], Tefnd0723[0][1], Tmmjs0723[0][2], Tmmjs0723[0][3], Tmmjs0723[0][4], Tmmjs0723[0][5], Tmmjs0723[0][6], Tmmjs0723[0][7], Tmmjs0723[0][8], Tmmjs0723[0][9], Tefnd0723[0][10], Tefnd0006[7][11]],
                   [Tefnd0723[1][0], Tefnd0723[1][1], Tmmjs0723[1][2], Tmmjs0723[1][3], Tmmjs0723[1][4], Tmmjs0723[1][5], Tmmjs0723[1][6], Tmmjs0723[1][7], Tmmjs0723[1][8], Tmmjs0723[1][9], Tefnd0723[1][10], Tefnd0723[1][11]],
                   [Tefnd0723[2][0], Tefnd0723[2][1], Tmmjs0723[2][2], Tmmjs0723[2][3], Tmmjs0723[2][4], Tmmjs0723[2][5], Tmmjs0723[2][6], Tmmjs0723[2][7], Tmmjs0723[2][8], Tmmjs0723[2][9], Tefnd0723[2][10], Tefnd0723[2][11]],
                   [Tefnd0723[3][0], Tefnd0723[3][1], Tmmjs0723[3][2], Tmmjs0723[3][3], Tmmjs0723[3][4], Tmmjs0723[3][5], Tmmjs0723[3][6], Tmmjs0723[3][7], Tmmjs0723[3][8], Tmmjs0723[3][9], Tefnd0723[3][10], Tefnd0723[3][11]],
                   [Tefnd0723[4][0], Tefnd0723[4][1], Tmmjs0723[4][2], Tmmjs0723[4][3], Tmmjs0723[4][4], Tmmjs0723[4][5], Tmmjs0723[4][6], Tmmjs0723[4][7], Tmmjs0723[4][8], Tmmjs0723[4][9], Tefnd0723[4][10], Tefnd0723[4][11]],
                   [Tefnd0723[5][0], Tefnd0723[5][1], Tmmjs0723[5][2], Tmmjs0723[5][3], Tmmjs0723[5][4], Tmmjs0723[5][5], Tmmjs0723[5][6], Tmmjs0723[5][7], Tmmjs0723[5][8], Tmmjs0723[5][9], Tefnd0723[5][10], Tefnd0723[5][11]],
                   [Tefnd0723[6][0], Tefnd0723[6][1], Tmmjs0723[6][2], Tmmjs0723[6][3], Tmmjs0723[6][4], Tmmjs0723[6][5], Tmmjs0723[6][6], Tmmjs0723[6][7], Tmmjs0723[6][8], Tmmjs0723[6][9], Tefnd0723[6][10], Tefnd0723[6][11]],
                   [Tefnd0723[7][0], Tefnd0723[7][1], Tmmjs0723[7][2], Tmmjs0723[7][3], Tmmjs0723[7][4], Tmmjs0723[7][5], Tmmjs0723[7][6], Tmmjs0723[7][7], Tmmjs0723[7][8], Tmmjs0723[7][9], Tefnd0723[7][10], Tefnd0723[7][11]],
                   [Tefnd0723[8][0], Tefnd0723[8][1], Tmmjs0723[8][2], Tmmjs0723[8][3], Tmmjs0723[8][4], Tmmjs0723[8][5], Tmmjs0723[8][6], Tmmjs0723[8][7], Tmmjs0723[8][8], Tmmjs0723[8][9], Tefnd0723[8][10], Tefnd0723[8][11]],
                   [Tefnd0723[9][0], Tefnd0723[9][1], Tmmjs0723[9][2], Tmmjs0723[9][3], Tmmjs0723[9][4], Tmmjs0723[9][5], Tmmjs0723[9][6], Tmmjs0723[9][7], Tmmjs0723[9][8], Tmmjs0723[9][9], Tefnd0723[9][10], Tefnd0723[9][11]],
                   [Tefnd0723[10][0], Tefnd0723[10][1], Tmmjs0723[10][2], Tmmjs0723[10][3], Tmmjs0723[10][4], Tmmjs0723[10][5], Tmmjs0723[10][6], Tmmjs0723[10][7], Tmmjs0723[10][8], Tmmjs0723[10][9], Tefnd0723[10][10], Tefnd0723[10][11]],
                   [Tefnd0723[11][0], Tefnd0723[11][1], Tmmjs0723[11][2], Tmmjs0723[11][3], Tmmjs0723[11][4], Tmmjs0723[11][5], Tmmjs0723[11][6], Tmmjs0723[11][7], Tmmjs0723[11][8], Tmmjs0723[11][9], Tefnd0723[11][10], Tefnd0723[11][11]],
                   [Tefnd0723[12][0], Tefnd0723[12][1], Tmmjs0723[12][2], Tmmjs0723[12][3], Tmmjs0723[12][4], Tmmjs0723[12][5], Tmmjs0723[12][6], Tmmjs0723[12][7], Tmmjs0723[12][8], Tmmjs0723[12][9], Tefnd0723[12][10], Tefnd0723[12][11]],
                   [Tefnd0723[13][0], Tefnd0723[13][1], Tmmjs0723[13][2], Tmmjs0723[13][3], Tmmjs0723[13][4], Tmmjs0723[13][5], Tmmjs0723[13][6], Tmmjs0723[13][7], Tmmjs0723[13][8], Tmmjs0723[13][9], Tefnd0723[13][10], Tefnd0723[13][11]],
                   [Tefnd0723[14][0], Tefnd0723[14][1], Tmmjs0723[14][2], Tmmjs0723[14][3], Tmmjs0723[14][4], Tmmjs0723[14][5], Tmmjs0723[14][6], Tmmjs0723[14][7], Tmmjs0723[14][8], Tmmjs0723[14][9], Tefnd0723[14][10], Tefnd0723[14][11]],
                   [Tefnd0723[15][0], Tefnd0723[15][1], Tmmjs0723[15][2], Tmmjs0723[15][3], Tmmjs0723[15][4], Tmmjs0723[15][5], Tmmjs0723[15][6], Tmmjs0723[15][7], Tmmjs0723[15][8], Tmmjs0723[15][9], Tefnd0723[15][10], Tefnd0723[15][11]],
                   [Tefnd0723[16][0], Tefnd0723[16][1], Tmmjs0723[16][2], Tmmjs0723[16][3], Tmmjs0723[16][4], Tmmjs0723[16][5], Tmmjs0723[16][6], Tmmjs0723[16][7], Tmmjs0723[16][8], Tmmjs0723[16][9], Tefnd0723[16][10], Tefnd0723[16][11]]])

THLIST = np.array([[1, 0, Tefnd0006[0][0]],
                   [1, 1, Tefnd0006[1][0]],
                   [1, 2, Tefnd0006[2][0]],
                   [1, 3, Tefnd0006[3][0]],
                   [1, 4, Tefnd0006[4][0]],
                   [1, 5, Tefnd0006[5][0]],
                   [1, 6, Tefnd0006[6][0]],
                   [1, 7, Tefnd0723[0][0]],
                   [1, 8, Tefnd0723[1][0]],
                   [1, 9, Tefnd0723[2][0]],
                   [1, 10, Tefnd0723[3][0]],
                   [1, 11, Tefnd0723[4][0]],
                   [1, 12, Tefnd0723[5][0]],
                   [1, 13, Tefnd0723[6][0]],
                   [1, 14, Tefnd0723[7][0]],
                   [1, 15, Tefnd0723[8][0]],
                   [1, 16, Tefnd0723[9][0]],
                   [1, 17, Tefnd0723[10][0]],
                   [1, 18, Tefnd0723[11][0]],
                   [1, 19, Tefnd0723[12][0]],
                   [1, 20, Tefnd0723[13][0]],
                   [1, 21, Tefnd0723[14][0]],
                   [1, 22, Tefnd0723[15][0]],
                   [1, 23, Tefnd0723[16][0]],
                   [2, 0, Tefnd0006[0][1]],
                   [2, 1, Tefnd0006[1][1]],
                   [2, 2, Tefnd0006[2][1]],
                   [2, 3, Tefnd0006[3][1]],
                   [2, 4, Tefnd0006[4][1]],
                   [2, 5, Tefnd0006[5][1]],
                   [2, 6, Tefnd0006[6][1]],
                   [2, 7, Tefnd0723[0][1]],
                   [2, 8, Tefnd0723[1][1]],
                   [2, 9, Tefnd0723[2][1]],
                   [2, 10, Tefnd0723[3][1]],
                   [2, 11, Tefnd0723[4][1]],
                   [2, 12, Tefnd0723[5][1]],
                   [2, 13, Tefnd0723[6][1]],
                   [2, 14, Tefnd0723[7][1]],
                   [2, 15, Tefnd0723[8][1]],
                   [2, 16, Tefnd0723[9][1]],
                   [2, 17, Tefnd0723[10][1]],
                   [2, 18, Tefnd0723[11][1]],
                   [2, 19, Tefnd0723[12][1]],
                   [2, 20, Tefnd0723[13][1]],
                   [2, 21, Tefnd0723[14][1]],
                   [2, 22, Tefnd0723[15][1]],
                   [2, 23, Tefnd0723[16][1]],
                   [3, 0, Tmmjs0006[0][2]],
                   [3, 1, Tmmjs0006[1][2]],
                   [3, 2, Tmmjs0006[2][2]],
                   [3, 3, Tmmjs0006[3][2]],
                   [3, 4, Tmmjs0006[4][2]],
                   [3, 5, Tmmjs0006[5][2]],
                   [3, 6, Tmmjs0006[6][2]],
                   [3, 7, Tmmjs0723[0][2]],
                   [3, 8, Tmmjs0723[1][2]],
                   [3, 9, Tmmjs0723[2][2]],
                   [3, 10, Tmmjs0723[3][2]],
                   [3, 11, Tmmjs0723[4][2]],
                   [3, 12, Tmmjs0723[5][2]],
                   [3, 13, Tmmjs0723[6][2]],
                   [3, 14, Tmmjs0723[7][2]],
                   [3, 15, Tmmjs0723[8][2]],
                   [3, 16, Tmmjs0723[9][2]],
                   [3, 17, Tmmjs0723[10][2]],
                   [3, 18, Tmmjs0723[11][2]],
                   [3, 19, Tmmjs0723[12][2]],
                   [3, 20, Tmmjs0723[13][2]],
                   [3, 21, Tmmjs0723[14][2]],
                   [3, 22, Tmmjs0723[15][2]],
                   [3, 23, Tmmjs0723[16][2]],
                   [4, 0, Tmmjs0006[0][3]],
                   [4, 1, Tmmjs0006[1][3]],
                   [4, 2, Tmmjs0006[2][3]],
                   [4, 3, Tmmjs0006[3][3]],
                   [4, 4, Tmmjs0006[4][3]],
                   [4, 5, Tmmjs0006[5][3]],
                   [4, 6, Tmmjs0006[6][3]],
                   [4, 7, Tmmjs0723[0][3]],
                   [4, 8, Tmmjs0723[1][3]],
                   [4, 9, Tmmjs0723[2][3]],
                   [4, 10, Tmmjs0723[3][3]],
                   [4, 11, Tmmjs0723[4][3]],
                   [4, 12, Tmmjs0723[5][3]],
                   [4, 13, Tmmjs0723[6][3]],
                   [4, 14, Tmmjs0723[7][3]],
                   [4, 15, Tmmjs0723[8][3]],
                   [4, 16, Tmmjs0723[9][3]],
                   [4, 17, Tmmjs0723[10][3]],
                   [4, 18, Tmmjs0723[11][3]],
                   [4, 19, Tmmjs0723[12][3]],
                   [4, 20, Tmmjs0723[13][3]],
                   [4, 21, Tmmjs0723[14][3]],
                   [4, 22, Tmmjs0723[15][3]],
                   [4, 23, Tmmjs0723[16][3]],
                   [5, 0, Tmmjs0006[0][4]],
                   [5, 1, Tmmjs0006[1][4]],
                   [5, 2, Tmmjs0006[2][4]],
                   [5, 3, Tmmjs0006[3][4]],
                   [5, 4, Tmmjs0006[4][4]],
                   [5, 5, Tmmjs0006[5][4]],
                   [5, 6, Tmmjs0006[6][4]],
                   [5, 7, Tmmjs0723[0][4]],
                   [5, 8, Tmmjs0723[1][4]],
                   [5, 9, Tmmjs0723[2][4]],
                   [5, 10, Tmmjs0723[3][4]],
                   [5, 11, Tmmjs0723[4][4]],
                   [5, 12, Tmmjs0723[5][4]],
                   [5, 13, Tmmjs0723[6][4]],
                   [5, 14, Tmmjs0723[7][4]],
                   [5, 15, Tmmjs0723[8][4]],
                   [5, 16, Tmmjs0723[9][4]],
                   [5, 17, Tmmjs0723[10][4]],
                   [5, 18, Tmmjs0723[11][4]],
                   [5, 19, Tmmjs0723[12][4]],
                   [5, 20, Tmmjs0723[13][4]],
                   [5, 21, Tmmjs0723[14][4]],
                   [5, 22, Tmmjs0723[15][4]],
                   [5, 23, Tmmjs0723[16][4]],
                   [6, 0, Tmmjs0006[0][5]],
                   [6, 1, Tmmjs0006[1][5]],
                   [6, 2, Tmmjs0006[2][5]],
                   [6, 3, Tmmjs0006[3][5]],
                   [6, 4, Tmmjs0006[4][5]],
                   [6, 5, Tmmjs0006[5][5]],
                   [6, 6, Tmmjs0006[6][5]],
                   [6, 7, Tmmjs0723[0][5]],
                   [6, 8, Tmmjs0723[1][5]],
                   [6, 9, Tmmjs0723[2][5]],
                   [6, 10, Tmmjs0723[3][5]],
                   [6, 11, Tmmjs0723[4][5]],
                   [6, 12, Tmmjs0723[5][5]],
                   [6, 13, Tmmjs0723[6][5]],
                   [6, 14, Tmmjs0723[7][5]],
                   [6, 15, Tmmjs0723[8][5]],
                   [6, 16, Tmmjs0723[9][5]],
                   [6, 17, Tmmjs0723[10][5]],
                   [6, 18, Tmmjs0723[11][5]],
                   [6, 19, Tmmjs0723[12][5]],
                   [6, 20, Tmmjs0723[13][5]],
                   [6, 21, Tmmjs0723[14][5]],
                   [6, 22, Tmmjs0723[15][5]],
                   [6, 23, Tmmjs0723[16][5]],
                   [7, 0, Tmmjs0006[0][6]],
                   [7, 1, Tmmjs0006[1][6]],
                   [7, 2, Tmmjs0006[2][6]],
                   [7, 3, Tmmjs0006[3][6]],
                   [7, 4, Tmmjs0006[4][6]],
                   [7, 5, Tmmjs0006[5][6]],
                   [7, 6, Tmmjs0006[6][6]],
                   [7, 7, Tmmjs0723[0][6]],
                   [7, 8, Tmmjs0723[1][6]],
                   [7, 9, Tmmjs0723[2][6]],
                   [7, 10, Tmmjs0723[3][6]],
                   [7, 11, Tmmjs0723[4][6]],
                   [7, 12, Tmmjs0723[5][6]],
                   [7, 13, Tmmjs0723[6][6]],
                   [7, 14, Tmmjs0723[7][6]],
                   [7, 15, Tmmjs0723[8][6]],
                   [7, 16, Tmmjs0723[9][6]],
                   [7, 17, Tmmjs0723[10][6]],
                   [7, 18, Tmmjs0723[11][6]],
                   [7, 19, Tmmjs0723[12][6]],
                   [7, 20, Tmmjs0723[13][6]],
                   [7, 21, Tmmjs0723[14][6]],
                   [7, 22, Tmmjs0723[15][6]],
                   [7, 23, Tmmjs0723[16][6]],
                   [8, 0, Tmmjs0006[0][7]],
                   [8, 1, Tmmjs0006[1][7]],
                   [8, 2, Tmmjs0006[2][7]],
                   [8, 3, Tmmjs0006[3][7]],
                   [8, 4, Tmmjs0006[4][7]],
                   [8, 5, Tmmjs0006[5][7]],
                   [8, 6, Tmmjs0006[6][7]],
                   [8, 7, Tmmjs0723[0][7]],
                   [8, 8, Tmmjs0723[1][7]],
                   [8, 9, Tmmjs0723[2][7]],
                   [8, 10, Tmmjs0723[3][7]],
                   [8, 11, Tmmjs0723[4][7]],
                   [8, 12, Tmmjs0723[5][7]],
                   [8, 13, Tmmjs0723[6][7]],
                   [8, 14, Tmmjs0723[7][7]],
                   [8, 15, Tmmjs0723[8][7]],
                   [8, 16, Tmmjs0723[9][7]],
                   [8, 17, Tmmjs0723[10][7]],
                   [8, 18, Tmmjs0723[11][7]],
                   [8, 19, Tmmjs0723[12][7]],
                   [8, 20, Tmmjs0723[13][7]],
                   [8, 21, Tmmjs0723[14][7]],
                   [8, 22, Tmmjs0723[15][7]],
                   [8, 23, Tmmjs0723[16][7]],
                   [9, 0, Tmmjs0006[0][8]],
                   [9, 1, Tmmjs0006[1][8]],
                   [9, 2, Tmmjs0006[2][8]],
                   [9, 3, Tmmjs0006[3][8]],
                   [9, 4, Tmmjs0006[4][8]],
                   [9, 5, Tmmjs0006[5][8]],
                   [9, 6, Tmmjs0006[6][8]],
                   [9, 7, Tmmjs0723[0][8]],
                   [9, 8, Tmmjs0723[1][8]],
                   [9, 9, Tmmjs0723[2][8]],
                   [9, 10, Tmmjs0723[3][8]],
                   [9, 11, Tmmjs0723[4][8]],
                   [9, 12, Tmmjs0723[5][8]],
                   [9, 13, Tmmjs0723[6][8]],
                   [9, 14, Tmmjs0723[7][8]],
                   [9, 15, Tmmjs0723[8][8]],
                   [9, 16, Tmmjs0723[9][8]],
                   [9, 17, Tmmjs0723[10][8]],
                   [9, 18, Tmmjs0723[11][8]],
                   [9, 19, Tmmjs0723[12][8]],
                   [9, 20, Tmmjs0723[13][8]],
                   [9, 21, Tmmjs0723[14][8]],
                   [9, 22, Tmmjs0723[15][8]],
                   [9, 23, Tmmjs0723[16][8]],
                   [10, 0, Tmmjs0006[0][9]],
                   [10, 1, Tmmjs0006[1][9]],
                   [10, 2, Tmmjs0006[2][9]],
                   [10, 3, Tmmjs0006[3][9]],
                   [10, 4, Tmmjs0006[4][9]],
                   [10, 5, Tmmjs0006[5][9]],
                   [10, 6, Tmmjs0006[6][9]],
                   [10, 7, Tmmjs0723[0][9]],
                   [10, 8, Tmmjs0723[1][9]],
                   [10, 9, Tmmjs0723[2][9]],
                   [10, 10, Tmmjs0723[3][9]],
                   [10, 11, Tmmjs0723[4][9]],
                   [10, 12, Tmmjs0723[5][9]],
                   [10, 13, Tmmjs0723[6][9]],
                   [10, 14, Tmmjs0723[7][9]],
                   [10, 15, Tmmjs0723[8][9]],
                   [10, 16, Tmmjs0723[9][9]],
                   [10, 17, Tmmjs0723[10][9]],
                   [10, 18, Tmmjs0723[11][9]],
                   [10, 19, Tmmjs0723[12][9]],
                   [10, 20, Tmmjs0723[13][9]],
                   [10, 21, Tmmjs0723[14][9]],
                   [10, 22, Tmmjs0723[15][9]],
                   [10, 23, Tmmjs0723[16][9]],
                   [11, 0, Tefnd0006[0][10]],
                   [11, 1, Tefnd0006[1][10]],
                   [11, 2, Tefnd0006[2][10]],
                   [11, 3, Tefnd0006[3][10]],
                   [11, 4, Tefnd0006[4][10]],
                   [11, 5, Tefnd0006[5][10]],
                   [11, 6, Tefnd0006[6][10]],
                   [11, 7, Tefnd0723[0][10]],
                   [11, 8, Tefnd0723[1][10]],
                   [11, 9, Tefnd0723[2][10]],
                   [11, 10, Tefnd0723[3][10]],
                   [11, 11, Tefnd0723[4][10]],
                   [11, 12, Tefnd0723[5][10]],
                   [11, 13, Tefnd0723[6][10]],
                   [11, 14, Tefnd0723[7][10]],
                   [11, 15, Tefnd0723[8][10]],
                   [11, 16, Tefnd0723[9][10]],
                   [11, 17, Tefnd0723[10][10]],
                   [11, 18, Tefnd0723[11][10]],
                   [11, 19, Tefnd0723[12][10]],
                   [11, 20, Tefnd0723[13][10]],
                   [11, 21, Tefnd0723[14][10]],
                   [11, 22, Tefnd0723[15][10]],
                   [11, 23, Tefnd0723[16][10]],
                   [12, 0, Tefnd0006[0][11]],
                   [12, 1, Tefnd0006[1][11]],
                   [12, 2, Tefnd0006[2][11]],
                   [12, 3, Tefnd0006[3][11]],
                   [12, 4, Tefnd0006[4][11]],
                   [12, 5, Tefnd0006[5][11]],
                   [12, 6, Tefnd0006[6][11]],
                   [12, 7, Tefnd0006[7][11]],
                   [12, 8, Tefnd0723[1][11]],
                   [12, 9, Tefnd0723[2][11]],
                   [12, 10, Tefnd0723[3][11]],
                   [12, 11, Tefnd0723[4][11]],
                   [12, 12, Tefnd0723[5][11]],
                   [12, 13, Tefnd0723[6][11]],
                   [12, 14, Tefnd0723[7][11]],
                   [12, 15, Tefnd0723[8][11]],
                   [12, 16, Tefnd0723[9][11]],
                   [12, 17, Tefnd0723[10][11]],
                   [12, 18, Tefnd0723[11][11]],
                   [12, 19, Tefnd0723[12][11]],
                   [12, 20, Tefnd0723[13][11]],
                   [12, 21, Tefnd0723[14][11]],
                   [12, 22, Tefnd0723[15][11]],
                   [12, 23, Tefnd0723[16][11]]])

TEMHOR2 = np.around(TEMHOR, decimals=1)
#print(TEMHOR2)
THLIST2 = np.around(THLIST, decimals=1)

#DFTH = np.loadtxt(THLIST2, delimiter = ' ')

DFTH = pd.DataFrame(data=THLIST2, columns=['mm','hr','tn'])

#print(DFTH)

#print(THLIST2)

print('Temperatura horaria media mensual')
THORMED = np.array([np.average(TEMHOR[:,0]), np.average(TEMHOR[:,1]), np.average(TEMHOR[:,2]), np.average(TEMHOR[:,3]), np.average(TEMHOR[:,4]), np.average(TEMHOR[:,5]), np.average(TEMHOR[:,6]), np.average(TEMHOR[:,7]), np.average(TEMHOR[:,8]), np.average(TEMHOR[:,9]), np.average(TEMHOR[:,10]), np.average(TEMHOR[:,11])])
THORMED2 = np.around(THORMED, decimals=1)

#TNMaxMin = '/'.join([p2,'TNMaxMin/' + str(estacion) + '.csv'])
    
DFTH.to_csv(pathtemphora, index=False, header = False, sep = ' ')

#with open(pathtemphora, 'w') as f:
#    for item in THLIST2:
#        item = str(item)
#        item = item.replace(']','')
        #item = item.replace(' ',',')
#        f.write("%s\n" % item)    

#print(THORMED2)



###############################################################################
###############################################################################
######           3.-  Humedad Horaria
###############################################################################
###############################################################################

print('HR horaria mensual')

#enero, febrero, noviembre y diciembre de 00:00 a 06:00
if Lat>=23.5 :
   if np.all(n)>=np.any(Hrmin) :
      HRefnd0006 = HRmin+(1-(0.023*(n-Hrmin)**3.436)*(np.exp(-0.421*(n-Hrmin))))*(HRmax-HRmin)
   else:  
      HRefnd0006 = HRmin+(1-(0.023*(n+24-Hrmin)**3.436)*(np.exp(-0.421*(n+24-Hrmin))))*(HRmax-HRmin)
else:
   if np.all(n)>=np.any(Hrmin) :
      HRefnd0006 = HRmin+(1-(0.096*(n-Hrmin)**2.422)*(np.exp(-0.339*(n-Hrmin))))*(HRmax-HRmin)
   else :
      HRefnd0006 = HRmin+(1-(0.096*(n+24-Hrmin)**2.422)*(np.exp(-0.339*(n+24-Hrmin))))*(HRmax-HRmin)

#enero, febrero, noviembre y diciembre de 07:00 a 23:00
if Lat>=23.5 :
   if np.any(n)>=np.all(Hrmin) :
      HRefnd0723 = HRmin+(1-(0.023*(m-Hrmin)**3.436)*(np.exp(-0.421*(m-Hrmin))))*(HRmax-HRmin)
   else:  
      HRefnd0723 = HRmin+(1-(0.023*(m+24-Hrmin)**3.436)*(np.exp(-0.421*(m+24-Hrmin))))*(HRmax-HRmin)
else:
   if np.any(n)>=np.all(Hrmin) :
      HRefnd0723 = HRmin+(1-(0.096*(m-Hrmin)**2.422)*(np.exp(-0.339*(m-Hrmin))))*(HRmax-HRmin)
   else :
      HRefnd0723 = HRmin+(1-(0.096*(m+24-Hrmin)**2.422)*(np.exp(-0.339*(m+24-Hrmin))))*(HRmax-HRmin)

#marzo, abril, mayo, junio, julio, agosto, 
#septiembre, octubre de 00:00 a 06:00
if Lat>=23.5 :
   if np.all(n)>=np.any(Hrmin) :
      HRmmjs0006 = HRmin+(1-(0.026*(n-Hrmin)**3.19)*(np.exp(-0.375*(n-Hrmin))))*(HRmax-HRmin)
   else:  
      HRmmjs0006 = HRmin+(1-(0.026*(n+24-Hrmin)**3.19)*(np.exp(-0.375*(n+24-Hrmin))))*(HRmax-HRmin)
else:
   if np.all(n)>=np.any(Hrmin) :
      HRmmjs0006 = HRmin+(1-(0.096*(n-Hrmin)**2.422)*(np.exp(-0.339*(n-Hrmin))))*(HRmax-HRmin)
   else :
      HRmmjs0006 = HRmin+(1-(0.096*(n+24-Hrmin)**2.422)*(np.exp(-0.339*(n+24-Hrmin))))*(HRmax-HRmin)

#marzo, abril, mayo, junio, julio, agosto, 
#septiembre, octubre de 00:07 a 23:00
if Lat>=23.5 :
   if np.any(n)>=np.all(Hrmin) :
      HRmmjs0723 = HRmin+(1-(0.026*(m-Hrmin)**3.19)*(np.exp(-0.375*(m-Hrmin))))*(HRmax-HRmin)
   else:  
      HRmmjs0723 = HRmin+(1-(0.026*(m+24-Hrmin)**3.19)*(np.exp(-0.375*(m+24-Hrmin))))*(HRmax-HRmin)
else:
   if np.any(n)>=np.all(Hrmin) :
      HRmmjs0723 = HRmin+(1-(0.096*(m-Hrmin)**2.422)*(np.exp(-0.339*(m-Hrmin))))*(HRmax-HRmin)
   else :
      HRmmjs0723 = HRmin+(1-(0.096*(m+24-Hrmin)**2.422)*(np.exp(-0.339*(m+24-Hrmin))))*(HRmax-HRmin)

HRHOR = np.array([[HRefnd0006[0][0], HRefnd0006[0][1], HRmmjs0006[0][2], HRmmjs0006[0][3], HRmmjs0006[0][4], HRmmjs0006[0][5], HRmmjs0006[0][6], HRmmjs0006[0][7], HRmmjs0006[0][8], HRmmjs0006[0][9], HRefnd0006[0][10], HRefnd0006[0][11]],
                   [HRefnd0006[1][0], HRefnd0006[1][1], HRmmjs0006[1][2], HRmmjs0006[1][3], HRmmjs0006[1][4], HRmmjs0006[1][5], HRmmjs0006[1][6], HRmmjs0006[1][7], HRmmjs0006[1][8], HRmmjs0006[1][9], HRefnd0006[1][10], HRefnd0006[1][11]],
                   [HRefnd0006[2][0], HRefnd0006[2][1], HRmmjs0006[2][2], HRmmjs0006[2][3], HRmmjs0006[2][4], HRmmjs0006[2][5], HRmmjs0006[2][6], HRmmjs0006[2][7], HRmmjs0006[2][8], HRmmjs0006[2][9], HRefnd0006[2][10], HRefnd0006[2][11]],
                   [HRefnd0006[3][0], HRefnd0006[3][1], HRmmjs0006[3][2], HRmmjs0006[3][3], HRmmjs0006[3][4], HRmmjs0006[3][5], HRmmjs0006[3][6], HRmmjs0006[3][7], HRmmjs0006[3][8], HRmmjs0006[3][9], HRefnd0006[3][10], HRefnd0006[3][11]],
                   [HRefnd0006[4][0], HRefnd0006[4][1], HRmmjs0006[4][2], HRmmjs0006[4][3], HRmmjs0006[4][4], HRmmjs0006[4][5], HRmmjs0006[4][6], HRmmjs0006[4][7], HRmmjs0006[4][8], HRmmjs0006[4][9], HRefnd0006[4][10], HRefnd0006[4][11]],
                   [HRefnd0006[5][0], HRefnd0006[5][1], HRmmjs0006[5][2], HRmmjs0006[5][3], HRmmjs0006[5][4], HRmmjs0006[5][5], HRmmjs0006[5][6], HRmmjs0006[5][7], HRmmjs0006[5][8], HRmmjs0006[5][9], HRefnd0006[5][10], HRefnd0006[5][11]],
                   [HRefnd0006[6][0], HRefnd0006[6][1], HRmmjs0006[6][2], HRmmjs0006[6][3], HRmmjs0006[6][4], HRmmjs0006[6][5], HRmmjs0006[6][6], HRmmjs0006[6][7], HRmmjs0006[6][8], HRmmjs0006[6][9], HRefnd0006[6][10], HRefnd0006[6][11]],
                   [HRefnd0723[0][0], HRefnd0723[0][1], HRmmjs0723[0][2], HRmmjs0723[0][3], HRmmjs0723[0][4], HRmmjs0723[0][5], HRmmjs0723[0][6], HRmmjs0723[0][7], HRmmjs0723[0][8], HRmmjs0723[0][9], HRefnd0723[0][10], HRefnd0006[7][11]],
                   [HRefnd0723[1][0], HRefnd0723[1][1], HRmmjs0723[1][2], HRmmjs0723[1][3], HRmmjs0723[1][4], HRmmjs0723[1][5], HRmmjs0723[1][6], HRmmjs0723[1][7], HRmmjs0723[1][8], HRmmjs0723[1][9], HRefnd0723[1][10], HRefnd0723[1][11]],
                   [HRefnd0723[2][0], HRefnd0723[2][1], HRmmjs0723[2][2], HRmmjs0723[2][3], HRmmjs0723[2][4], HRmmjs0723[2][5], HRmmjs0723[2][6], HRmmjs0723[2][7], HRmmjs0723[2][8], HRmmjs0723[2][9], HRefnd0723[2][10], HRefnd0723[2][11]],
                   [HRefnd0723[3][0], HRefnd0723[3][1], HRmmjs0723[3][2], HRmmjs0723[3][3], HRmmjs0723[3][4], HRmmjs0723[3][5], HRmmjs0723[3][6], HRmmjs0723[3][7], HRmmjs0723[3][8], HRmmjs0723[3][9], HRefnd0723[3][10], HRefnd0723[3][11]],
                   [HRefnd0723[4][0], HRefnd0723[4][1], HRmmjs0723[4][2], HRmmjs0723[4][3], HRmmjs0723[4][4], HRmmjs0723[4][5], HRmmjs0723[4][6], HRmmjs0723[4][7], HRmmjs0723[4][8], HRmmjs0723[4][9], HRefnd0723[4][10], HRefnd0723[4][11]],
                   [HRefnd0723[5][0], HRefnd0723[5][1], HRmmjs0723[5][2], HRmmjs0723[5][3], HRmmjs0723[5][4], HRmmjs0723[5][5], HRmmjs0723[5][6], HRmmjs0723[5][7], HRmmjs0723[5][8], HRmmjs0723[5][9], HRefnd0723[5][10], HRefnd0723[5][11]],
                   [HRefnd0723[6][0], HRefnd0723[6][1], HRmmjs0723[6][2], HRmmjs0723[6][3], HRmmjs0723[6][4], HRmmjs0723[6][5], HRmmjs0723[6][6], HRmmjs0723[6][7], HRmmjs0723[6][8], HRmmjs0723[6][9], HRefnd0723[6][10], HRefnd0723[6][11]],
                   [HRefnd0723[7][0], HRefnd0723[7][1], HRmmjs0723[7][2], HRmmjs0723[7][3], HRmmjs0723[7][4], HRmmjs0723[7][5], HRmmjs0723[7][6], HRmmjs0723[7][7], HRmmjs0723[7][8], HRmmjs0723[7][9], HRefnd0723[7][10], HRefnd0723[7][11]],
                   [HRefnd0723[8][0], HRefnd0723[8][1], HRmmjs0723[8][2], HRmmjs0723[8][3], HRmmjs0723[8][4], HRmmjs0723[8][5], HRmmjs0723[8][6], HRmmjs0723[8][7], HRmmjs0723[8][8], HRmmjs0723[8][9], HRefnd0723[8][10], HRefnd0723[8][11]],
                   [HRefnd0723[9][0], HRefnd0723[9][1], HRmmjs0723[9][2], HRmmjs0723[9][3], HRmmjs0723[9][4], HRmmjs0723[9][5], HRmmjs0723[9][6], HRmmjs0723[9][7], HRmmjs0723[9][8], HRmmjs0723[9][9], HRefnd0723[9][10], HRefnd0723[9][11]],
                   [HRefnd0723[10][0], HRefnd0723[10][1], HRmmjs0723[10][2], HRmmjs0723[10][3], HRmmjs0723[10][4], HRmmjs0723[10][5], HRmmjs0723[10][6], HRmmjs0723[10][7], HRmmjs0723[10][8], HRmmjs0723[10][9], HRefnd0723[10][10], HRefnd0723[10][11]],
                   [HRefnd0723[11][0], HRefnd0723[11][1], HRmmjs0723[11][2], HRmmjs0723[11][3], HRmmjs0723[11][4], HRmmjs0723[11][5], HRmmjs0723[11][6], HRmmjs0723[11][7], HRmmjs0723[11][8], HRmmjs0723[11][9], HRefnd0723[11][10], HRefnd0723[11][11]],
                   [HRefnd0723[12][0], HRefnd0723[12][1], HRmmjs0723[12][2], HRmmjs0723[12][3], HRmmjs0723[12][4], HRmmjs0723[12][5], HRmmjs0723[12][6], HRmmjs0723[12][7], HRmmjs0723[12][8], HRmmjs0723[12][9], HRefnd0723[12][10], HRefnd0723[12][11]],
                   [HRefnd0723[13][0], HRefnd0723[13][1], HRmmjs0723[13][2], HRmmjs0723[13][3], HRmmjs0723[13][4], HRmmjs0723[13][5], HRmmjs0723[13][6], HRmmjs0723[13][7], HRmmjs0723[13][8], HRmmjs0723[13][9], HRefnd0723[13][10], HRefnd0723[13][11]],
                   [HRefnd0723[14][0], HRefnd0723[14][1], HRmmjs0723[14][2], HRmmjs0723[14][3], HRmmjs0723[14][4], HRmmjs0723[14][5], HRmmjs0723[14][6], HRmmjs0723[14][7], HRmmjs0723[14][8], HRmmjs0723[14][9], HRefnd0723[14][10], HRefnd0723[14][11]],
                   [HRefnd0723[15][0], HRefnd0723[15][1], HRmmjs0723[15][2], HRmmjs0723[15][3], HRmmjs0723[15][4], HRmmjs0723[15][5], HRmmjs0723[15][6], HRmmjs0723[15][7], HRmmjs0723[15][8], HRmmjs0723[15][9], HRefnd0723[15][10], HRefnd0723[15][11]],
                   [HRefnd0723[16][0], HRefnd0723[16][1], HRmmjs0723[16][2], HRmmjs0723[16][3], HRmmjs0723[16][4], HRmmjs0723[16][5], HRmmjs0723[16][6], HRmmjs0723[16][7], HRmmjs0723[16][8], HRmmjs0723[16][9], HRefnd0723[16][10], HRefnd0723[16][11]]])

HRLIST = np.array([[1, 0, HRefnd0006[0][0]],
                   [1, 1, HRefnd0006[1][0]],
                   [1, 2, HRefnd0006[2][0]],
                   [1, 3, HRefnd0006[3][0]],
                   [1, 4, HRefnd0006[4][0]],
                   [1, 5, HRefnd0006[5][0]],
                   [1, 6, HRefnd0006[6][0]],
                   [1, 7, HRefnd0723[0][0]],
                   [1, 8, HRefnd0723[1][0]],
                   [1, 9, HRefnd0723[2][0]],
                   [1, 10, HRefnd0723[3][0]],
                   [1, 11, HRefnd0723[4][0]],
                   [1, 12, HRefnd0723[5][0]],
                   [1, 13, HRefnd0723[6][0]],
                   [1, 14, HRefnd0723[7][0]],
                   [1, 15, HRefnd0723[8][0]],
                   [1, 16, HRefnd0723[9][0]],
                   [1, 17, HRefnd0723[10][0]],
                   [1, 18, HRefnd0723[11][0]],
                   [1, 19, HRefnd0723[12][0]],
                   [1, 20, HRefnd0723[13][0]],
                   [1, 21, HRefnd0723[14][0]],
                   [1, 22, HRefnd0723[15][0]],
                   [1, 23, HRefnd0723[16][0]],
                   [2, 0, HRefnd0006[0][1]],
                   [2, 1, HRefnd0006[1][1]],
                   [2, 2, HRefnd0006[2][1]],
                   [2, 3, HRefnd0006[3][1]],
                   [2, 4, HRefnd0006[4][1]],
                   [2, 5, HRefnd0006[5][1]],
                   [2, 6, HRefnd0006[6][1]],
                   [2, 7, HRefnd0723[0][1]],
                   [2, 8, HRefnd0723[1][1]],
                   [2, 9, HRefnd0723[2][1]],
                   [2, 10, HRefnd0723[3][1]],
                   [2, 11, HRefnd0723[4][1]],
                   [2, 12, HRefnd0723[5][1]],
                   [2, 13, HRefnd0723[6][1]],
                   [2, 14, HRefnd0723[7][1]],
                   [2, 15, HRefnd0723[8][1]],
                   [2, 16, HRefnd0723[9][1]],
                   [2, 17, HRefnd0723[10][1]],
                   [2, 18, HRefnd0723[11][1]],
                   [2, 19, HRefnd0723[12][1]],
                   [2, 20, HRefnd0723[13][1]],
                   [2, 21, HRefnd0723[14][1]],
                   [2, 22, HRefnd0723[15][1]],
                   [2, 23, HRefnd0723[16][1]],
                   [3, 0, HRmmjs0006[0][2]],
                   [3, 1, HRmmjs0006[1][2]],
                   [3, 2, HRmmjs0006[2][2]],
                   [3, 3, HRmmjs0006[3][2]],
                   [3, 4, HRmmjs0006[4][2]],
                   [3, 5, HRmmjs0006[5][2]],
                   [3, 6, HRmmjs0006[6][2]],
                   [3, 7, HRmmjs0723[0][2]],
                   [3, 8, HRmmjs0723[1][2]],
                   [3, 9, HRmmjs0723[2][2]],
                   [3, 10, HRmmjs0723[3][2]],
                   [3, 11, HRmmjs0723[4][2]],
                   [3, 12, HRmmjs0723[5][2]],
                   [3, 13, HRmmjs0723[6][2]],
                   [3, 14, HRmmjs0723[7][2]],
                   [3, 15, HRmmjs0723[8][2]],
                   [3, 16, HRmmjs0723[9][2]],
                   [3, 17, HRmmjs0723[10][2]],
                   [3, 18, HRmmjs0723[11][2]],
                   [3, 19, HRmmjs0723[12][2]],
                   [3, 20, HRmmjs0723[13][2]],
                   [3, 21, HRmmjs0723[14][2]],
                   [3, 22, HRmmjs0723[15][2]],
                   [3, 23, HRmmjs0723[16][2]],
                   [4, 0, HRmmjs0006[0][3]],
                   [4, 1, HRmmjs0006[1][3]],
                   [4, 2, HRmmjs0006[2][3]],
                   [4, 3, HRmmjs0006[3][3]],
                   [4, 4, HRmmjs0006[4][3]],
                   [4, 5, HRmmjs0006[5][3]],
                   [4, 6, HRmmjs0006[6][3]],
                   [4, 7, HRmmjs0723[0][3]],
                   [4, 8, HRmmjs0723[1][3]],
                   [4, 9, HRmmjs0723[2][3]],
                   [4, 10, HRmmjs0723[3][3]],
                   [4, 11, HRmmjs0723[4][3]],
                   [4, 12, HRmmjs0723[5][3]],
                   [4, 13, HRmmjs0723[6][3]],
                   [4, 14, HRmmjs0723[7][3]],
                   [4, 15, HRmmjs0723[8][3]],
                   [4, 16, HRmmjs0723[9][3]],
                   [4, 17, HRmmjs0723[10][3]],
                   [4, 18, HRmmjs0723[11][3]],
                   [4, 19, HRmmjs0723[12][3]],
                   [4, 20, HRmmjs0723[13][3]],
                   [4, 21, HRmmjs0723[14][3]],
                   [4, 22, HRmmjs0723[15][3]],
                   [4, 23, HRmmjs0723[16][3]],
                   [5, 0, HRmmjs0006[0][4]],
                   [5, 1, HRmmjs0006[1][4]],
                   [5, 2, HRmmjs0006[2][4]],
                   [5, 3, HRmmjs0006[3][4]],
                   [5, 4, HRmmjs0006[4][4]],
                   [5, 5, HRmmjs0006[5][4]],
                   [5, 6, HRmmjs0006[6][4]],
                   [5, 7, HRmmjs0723[0][4]],
                   [5, 8, HRmmjs0723[1][4]],
                   [5, 9, HRmmjs0723[2][4]],
                   [5, 10, HRmmjs0723[3][4]],
                   [5, 11, HRmmjs0723[4][4]],
                   [5, 12, HRmmjs0723[5][4]],
                   [5, 13, HRmmjs0723[6][4]],
                   [5, 14, HRmmjs0723[7][4]],
                   [5, 15, HRmmjs0723[8][4]],
                   [5, 16, HRmmjs0723[9][4]],
                   [5, 17, HRmmjs0723[10][4]],
                   [5, 18, HRmmjs0723[11][4]],
                   [5, 19, HRmmjs0723[12][4]],
                   [5, 20, HRmmjs0723[13][4]],
                   [5, 21, HRmmjs0723[14][4]],
                   [5, 22, HRmmjs0723[15][4]],
                   [5, 23, HRmmjs0723[16][4]],
                   [6, 0, HRmmjs0006[0][5]],
                   [6, 1, HRmmjs0006[1][5]],
                   [6, 2, HRmmjs0006[2][5]],
                   [6, 3, HRmmjs0006[3][5]],
                   [6, 4, HRmmjs0006[4][5]],
                   [6, 5, HRmmjs0006[5][5]],
                   [6, 6, HRmmjs0006[6][5]],
                   [6, 7, HRmmjs0723[0][5]],
                   [6, 8, HRmmjs0723[1][5]],
                   [6, 9, HRmmjs0723[2][5]],
                   [6, 10, HRmmjs0723[3][5]],
                   [6, 11, HRmmjs0723[4][5]],
                   [6, 12, HRmmjs0723[5][5]],
                   [6, 13, HRmmjs0723[6][5]],
                   [6, 14, HRmmjs0723[7][5]],
                   [6, 15, HRmmjs0723[8][5]],
                   [6, 16, HRmmjs0723[9][5]],
                   [6, 17, HRmmjs0723[10][5]],
                   [6, 18, HRmmjs0723[11][5]],
                   [6, 19, HRmmjs0723[12][5]],
                   [6, 20, HRmmjs0723[13][5]],
                   [6, 21, HRmmjs0723[14][5]],
                   [6, 22, HRmmjs0723[15][5]],
                   [6, 23, HRmmjs0723[16][5]],
                   [7, 0, HRmmjs0006[0][6]],
                   [7, 1, HRmmjs0006[1][6]],
                   [7, 2, HRmmjs0006[2][6]],
                   [7, 3, HRmmjs0006[3][6]],
                   [7, 4, HRmmjs0006[4][6]],
                   [7, 5, HRmmjs0006[5][6]],
                   [7, 6, HRmmjs0006[6][6]],
                   [7, 7, HRmmjs0723[0][6]],
                   [7, 8, HRmmjs0723[1][6]],
                   [7, 9, HRmmjs0723[2][6]],
                   [7, 10, HRmmjs0723[3][6]],
                   [7, 11, HRmmjs0723[4][6]],
                   [7, 12, HRmmjs0723[5][6]],
                   [7, 13, HRmmjs0723[6][6]],
                   [7, 14, HRmmjs0723[7][6]],
                   [7, 15, HRmmjs0723[8][6]],
                   [7, 16, HRmmjs0723[9][6]],
                   [7, 17, HRmmjs0723[10][6]],
                   [7, 18, HRmmjs0723[11][6]],
                   [7, 19, HRmmjs0723[12][6]],
                   [7, 20, HRmmjs0723[13][6]],
                   [7, 21, HRmmjs0723[14][6]],
                   [7, 22, HRmmjs0723[15][6]],
                   [7, 23, HRmmjs0723[16][6]],
                   [8, 0, HRmmjs0006[0][7]],
                   [8, 1, HRmmjs0006[1][7]],
                   [8, 2, HRmmjs0006[2][7]],
                   [8, 3, HRmmjs0006[3][7]],
                   [8, 4, HRmmjs0006[4][7]],
                   [8, 5, HRmmjs0006[5][7]],
                   [8, 6, HRmmjs0006[6][7]],
                   [8, 7, HRmmjs0723[0][7]],
                   [8, 8, HRmmjs0723[1][7]],
                   [8, 9, HRmmjs0723[2][7]],
                   [8, 10, HRmmjs0723[3][7]],
                   [8, 11, HRmmjs0723[4][7]],
                   [8, 12, HRmmjs0723[5][7]],
                   [8, 13, HRmmjs0723[6][7]],
                   [8, 14, HRmmjs0723[7][7]],
                   [8, 15, HRmmjs0723[8][7]],
                   [8, 16, HRmmjs0723[9][7]],
                   [8, 17, HRmmjs0723[10][7]],
                   [8, 18, HRmmjs0723[11][7]],
                   [8, 19, HRmmjs0723[12][7]],
                   [8, 20, HRmmjs0723[13][7]],
                   [8, 21, HRmmjs0723[14][7]],
                   [8, 22, HRmmjs0723[15][7]],
                   [8, 23, HRmmjs0723[16][7]],
                   [9, 0, HRmmjs0006[0][8]],
                   [9, 1, HRmmjs0006[1][8]],
                   [9, 2, HRmmjs0006[2][8]],
                   [9, 3, HRmmjs0006[3][8]],
                   [9, 4, HRmmjs0006[4][8]],
                   [9, 5, HRmmjs0006[5][8]],
                   [9, 6, HRmmjs0006[6][8]],
                   [9, 7, HRmmjs0723[0][8]],
                   [9, 8, HRmmjs0723[1][8]],
                   [9, 9, HRmmjs0723[2][8]],
                   [9, 10, HRmmjs0723[3][8]],
                   [9, 11, HRmmjs0723[4][8]],
                   [9, 12, HRmmjs0723[5][8]],
                   [9, 13, HRmmjs0723[6][8]],
                   [9, 14, HRmmjs0723[7][8]],
                   [9, 15, HRmmjs0723[8][8]],
                   [9, 16, HRmmjs0723[9][8]],
                   [9, 17, HRmmjs0723[10][8]],
                   [9, 18, HRmmjs0723[11][8]],
                   [9, 19, HRmmjs0723[12][8]],
                   [9, 20, HRmmjs0723[13][8]],
                   [9, 21, HRmmjs0723[14][8]],
                   [9, 22, HRmmjs0723[15][8]],
                   [9, 23, HRmmjs0723[16][8]],
                   [10, 0, HRmmjs0006[0][9]],
                   [10, 1, HRmmjs0006[1][9]],
                   [10, 2, HRmmjs0006[2][9]],
                   [10, 3, HRmmjs0006[3][9]],
                   [10, 4, HRmmjs0006[4][9]],
                   [10, 5, HRmmjs0006[5][9]],
                   [10, 6, HRmmjs0006[6][9]],
                   [10, 7, HRmmjs0723[0][9]],
                   [10, 8, HRmmjs0723[1][9]],
                   [10, 9, HRmmjs0723[2][9]],
                   [10, 10, HRmmjs0723[3][9]],
                   [10, 11, HRmmjs0723[4][9]],
                   [10, 12, HRmmjs0723[5][9]],
                   [10, 13, HRmmjs0723[6][9]],
                   [10, 14, HRmmjs0723[7][9]],
                   [10, 15, HRmmjs0723[8][9]],
                   [10, 16, HRmmjs0723[9][9]],
                   [10, 17, HRmmjs0723[10][9]],
                   [10, 18, HRmmjs0723[11][9]],
                   [10, 19, HRmmjs0723[12][9]],
                   [10, 20, HRmmjs0723[13][9]],
                   [10, 21, HRmmjs0723[14][9]],
                   [10, 22, HRmmjs0723[15][9]],
                   [10, 23, HRmmjs0723[16][9]],
                   [11, 0, HRefnd0006[0][10]],
                   [11, 1, HRefnd0006[1][10]],
                   [11, 2, HRefnd0006[2][10]],
                   [11, 3, HRefnd0006[3][10]],
                   [11, 4, HRefnd0006[4][10]],
                   [11, 5, HRefnd0006[5][10]],
                   [11, 6, HRefnd0006[6][10]],
                   [11, 7, HRefnd0723[0][10]],
                   [11, 8, HRefnd0723[1][10]],
                   [11, 9, HRefnd0723[2][10]],
                   [11, 10, HRefnd0723[3][10]],
                   [11, 11, HRefnd0723[4][10]],
                   [11, 12, HRefnd0723[5][10]],
                   [11, 13, HRefnd0723[6][10]],
                   [11, 14, HRefnd0723[7][10]],
                   [11, 15, HRefnd0723[8][10]],
                   [11, 16, HRefnd0723[9][10]],
                   [11, 17, HRefnd0723[10][10]],
                   [11, 18, HRefnd0723[11][10]],
                   [11, 19, HRefnd0723[12][10]],
                   [11, 20, HRefnd0723[13][10]],
                   [11, 21, HRefnd0723[14][10]],
                   [11, 22, HRefnd0723[15][10]],
                   [11, 23, HRefnd0723[16][10]],
                   [12, 0, HRefnd0006[0][11]],
                   [12, 1, HRefnd0006[1][11]],
                   [12, 2, HRefnd0006[2][11]],
                   [12, 3, HRefnd0006[3][11]],
                   [12, 4, HRefnd0006[4][11]],
                   [12, 5, HRefnd0006[5][11]],
                   [12, 6, HRefnd0006[6][11]],
                   [12, 7, HRefnd0006[7][11]],
                   [12, 8, HRefnd0723[1][11]],
                   [12, 9, HRefnd0723[2][11]],
                   [12, 10, HRefnd0723[3][11]],
                   [12, 11, HRefnd0723[4][11]],
                   [12, 12, HRefnd0723[5][11]],
                   [12, 13, HRefnd0723[6][11]],
                   [12, 14, HRefnd0723[7][11]],
                   [12, 15, HRefnd0723[8][11]],
                   [12, 16, HRefnd0723[9][11]],
                   [12, 17, HRefnd0723[10][11]],
                   [12, 18, HRefnd0723[11][11]],
                   [12, 19, HRefnd0723[12][11]],
                   [12, 20, HRefnd0723[13][11]],
                   [12, 21, HRefnd0723[14][11]],
                   [12, 22, HRefnd0723[15][11]],
                   [12, 23, HRefnd0723[16][11]]])

HRHOR2 = np.around(HRHOR, decimals=0)
#print(HRHOR2)
HRLIST2 = np.around(HRLIST, decimals=0)
#print(HRLIST2)

print('Humedad relativa horaria media mensual')
HRHORMED = np.array([np.average(HRHOR[:,0]), np.average(HRHOR[:,1]), np.average(HRHOR[:,2]), np.average(HRHOR[:,3]), np.average(HRHOR[:,4]), np.average(HRHOR[:,5]), np.average(HRHOR[:,6]), np.average(HRHOR[:,7]), np.average(HRHOR[:,8]), np.average(HRHOR[:,9]), np.average(HRHOR[:,10]), np.average(HRHOR[:,11])])
HRHORMED2 = np.around(HRHORMED, decimals=1)

DFHR = pd.DataFrame(data=HRLIST2, columns=['mm','hr','tn'])

DFHR.to_csv(pathhumhora, index=False, header = False, sep = ' ')

#with open(pathhumhora, 'w') as f1:
#    for item in HRLIST2:
#        f1.write("%s\n" % item)  

#print(HRHORMED2)

###############################################################################
###############################################################################
######           4.- INDICES BIOCLIMATICOS
###############################################################################
###############################################################################

###############################################################################
######           4.1.- Humidex
###############################################################################

##### CALCULANDO e #####
#print('Valores de e')
e = (6.115+(0.4219*TEMHOR)+(0.014206*TEMHOR**2)+(0.0003046*TEMHOR**3)+(0.0000032*TEMHOR**4))*(HRHOR/100)
e2 = np.around(e, decimals=1)
#print(e2)

##### CALCULANDO INDICE HUMIDEX #####
#print('humidex')
humidex = TEMHOR+(0.5555*(e-10))
humidex2 = np.around(humidex, decimals=1)
#print(humidex2)

##### TEMPERATURA PREFERENTE #####
#print('Temperatura preferente')
Tp = (0.31*THORMED)+17.8
Tp2 = np.around(Tp, decimals=1)
#print(Tp2)

##### e con HR = 50% #####
#print('Valores de e con HR = 50%')
ec = (6.115+(0.421915*Tp2)+(0.014206*(Tp2**2))+(0.0003046*(Tp2**3))+(0.0000032*(Tp2**4)))*(0.5)
ec = np.around(ec, decimals=1)
#print(ec)

##### HUMIDEX PREFERENTE #####
#print('humidex preferente')
hmdxp = Tp+(0.5555*(ec-10))
hmdxp2 = np.around(hmdxp, decimals=1)
#print(hmdxp2)

###############################################################################
######           Climograma
###############################################################################

#print('Climograma')
#print('INSTRUCCIONES: El climograma contiene valores entre -4 y 4 cada uno de los cuales indica una de las siguientes sensaciones termicas: ')
#print(      ' 4 = Calor extremo   (Color rojo oscuro) ')
#print(      ' 3 = Mucho calor     (Color rojo) ')
#print(      ' 2 = Calor moderado  (Color naranja) ')
#print(      ' 1 = Calor ligero    (Color amarillo) ')
#print(      ' 0 = Comfort         (Color blanco) ')
#print(      ' -1 = Frio ligero    (Color verde claro) ')
#print(      ' -2 = Frio moderado  (Color verde oscuro) ')
#print(      ' -3 = Mucho frio     (Color azul claro) ')
#print(      ' -4 = Frio Extremo   (Color azul oscuro) ')

En = []
for cell in humidex[:,0]:
        if (hmdxp[0]+10.5) < cell :
           En.append(4)
        elif (hmdxp[0]+7.5) < cell <= (hmdxp[0]+10.5) :
           En.append(3)
        elif (hmdxp[0]+4.5) < cell <= (hmdxp[0]+7.5) :
           En.append(2)
        elif (hmdxp[0]+1.5) < cell <= (hmdxp[0]+4.5) :
           En.append(1)
        elif (hmdxp[0]-1.5) <= cell <= (hmdxp[0]+1.5) :
           En.append(0)
        elif (hmdxp[0]-4.5) <= cell < (hmdxp[0]-1.5) :
           En.append(-1)
        elif (hmdxp[0]-7.5) <= cell < (hmdxp[0]-4.5) :
           En.append(-2)
        elif (hmdxp[0]-10.5) <= cell < (hmdxp[0]-7.5) :
           En.append(-3)
        else:
           En.append(-4)
Fe = []
for cell in humidex[:,1]:
        if (hmdxp[1]+10.5) < cell :
           Fe.append(4)
        elif (hmdxp[1]+7.5) < cell <= (hmdxp[1]+10.5) :
           Fe.append(3)
        elif (hmdxp[1]+4.5) < cell <= (hmdxp[1]+7.5) :
           Fe.append(2)
        elif (hmdxp[1]+1.5) < cell <= (hmdxp[1]+4.5) :
           Fe.append(1)
        elif (hmdxp[1]-1.5) <= cell <= (hmdxp[1]+1.5) :
           Fe.append(0)
        elif (hmdxp[1]-4.5) <= cell < (hmdxp[1]-1.5) :
           Fe.append(-1)
        elif (hmdxp[1]-7.5) <= cell < (hmdxp[1]-4.5) :
           Fe.append(-2)
        elif (hmdxp[1]-10.5) <= cell < (hmdxp[1]-7.5) :
           Fe.append(-3)
        else:
           Fe.append(-4)
Mz = []
for cell in humidex[:,2]:
        if (hmdxp[2]+10.5) < cell :
           Mz.append(4)
        elif (hmdxp[2]+7.5) < cell <= (hmdxp[2]+10.5) :
           Mz.append(3)
        elif (hmdxp[2]+4.5) < cell <= (hmdxp[2]+7.5) :
           Mz.append(2)
        elif (hmdxp[2]+1.5) < cell <= (hmdxp[2]+4.5) :
           Mz.append(1)
        elif (hmdxp[2]-1.5) <= cell <= (hmdxp[2]+1.5) :
           Mz.append(0)
        elif (hmdxp[2]-4.5) <= cell < (hmdxp[2]-1.5) :
           Mz.append(-1)
        elif (hmdxp[2]-7.5) <= cell < (hmdxp[2]-4.5) :
           Mz.append(-2)
        elif (hmdxp[2]-10.5) <= cell < (hmdxp[2]-7.5) :
           Mz.append(-3)
        else:
           Mz.append(-4)
Ab = []
for cell in humidex[:,3]:
        if (hmdxp[3]+10.5) < cell :
           Ab.append(4)
        elif (hmdxp[3]+7.5) < cell <= (hmdxp[3]+10.5) :
           Ab.append(3)
        elif (hmdxp[3]+4.5) < cell <= (hmdxp[3]+7.5) :
           Ab.append(2)
        elif (hmdxp[3]+1.5) < cell <= (hmdxp[3]+4.5) :
           Ab.append(1)
        elif (hmdxp[3]-1.5) <= cell <= (hmdxp[3]+1.5) :
           Ab.append(0)
        elif (hmdxp[3]-4.5) <= cell < (hmdxp[3]-1.5) :
           Ab.append(-1)
        elif (hmdxp[3]-7.5) <= cell < (hmdxp[3]-4.5) :
           Ab.append(-2)
        elif (hmdxp[3]-10.5) <= cell < (hmdxp[3]-7.5) :
           Ab.append(-3)
        else:
           Ab.append(-4)
My = []
for cell in humidex[:,4]:
        if (hmdxp[4]+10.5) < cell :
           My.append(4)
        elif (hmdxp[4]+7.5) < cell <= (hmdxp[4]+10.5) :
           My.append(3)
        elif (hmdxp[4]+4.5) < cell <= (hmdxp[4]+7.5) :
           My.append(2)
        elif (hmdxp[4]+1.5) < cell <= (hmdxp[4]+4.5) :
           My.append(1)
        elif (hmdxp[4]-1.5) <= cell <= (hmdxp[4]+1.5) :
           My.append(0)
        elif (hmdxp[4]-4.5) <= cell < (hmdxp[4]-1.5) :
           My.append(-1)
        elif (hmdxp[4]-7.5) <= cell < (hmdxp[4]-4.5) :
           My.append(-2)
        elif (hmdxp[4]-10.5) <= cell < (hmdxp[4]-7.5) :
           My.append(-3)
        else:
           My.append(-4)
Jn = []
for cell in humidex[:,5]:
        if (hmdxp[5]+10.5) < cell :
           Jn.append(4)
        elif (hmdxp[5]+7.5) < cell <= (hmdxp[5]+10.5) :
           Jn.append(3)
        elif (hmdxp[5]+4.5) < cell <= (hmdxp[5]+7.5) :
           Jn.append(2)
        elif (hmdxp[5]+1.5) < cell <= (hmdxp[5]+4.5) :
           Jn.append(1)
        elif (hmdxp[5]-1.5) <= cell <= (hmdxp[5]+1.5) :
           Jn.append(0)
        elif (hmdxp[5]-4.5) <= cell < (hmdxp[5]-1.5) :
           Jn.append(-1)
        elif (hmdxp[5]-7.5) <= cell < (hmdxp[5]-4.5) :
           Jn.append(-2)
        elif (hmdxp[5]-10.5) <= cell < (hmdxp[5]-7.5) :
           Jn.append(-3)
        else:
           Jn.append(-4)
Jl = []
for cell in humidex[:,6]:
        if (hmdxp[6]+10.5) < cell :
           Jl.append(4)
        elif (hmdxp[6]+7.5) < cell <= (hmdxp[6]+10.5) :
           Jl.append(3)
        elif (hmdxp[6]+4.5) < cell <= (hmdxp[6]+7.5) :
           Jl.append(2)
        elif (hmdxp[6]+1.5) < cell <= (hmdxp[6]+4.5) :
           Jl.append(1)
        elif (hmdxp[6]-1.5) <= cell <= (hmdxp[6]+1.5) :
           Jl.append(0)
        elif (hmdxp[6]-4.5) <= cell < (hmdxp[6]-1.5) :
           Jl.append(-1)
        elif (hmdxp[6]-7.5) <= cell < (hmdxp[6]-4.5) :
           Jl.append(-2)
        elif (hmdxp[6]-10.5) <= cell < (hmdxp[6]-7.5) :
           Jl.append(-3)
        else:
           Jl.append(-4)
Ag = []
for cell in humidex[:,7]:
        if (hmdxp[7]+10.5) < cell :
           Ag.append(4)
        elif (hmdxp[7]+7.5) < cell <= (hmdxp[7]+10.5) :
           Ag.append(3)
        elif (hmdxp[7]+4.5) < cell <= (hmdxp[7]+7.5) :
           Ag.append(2)
        elif (hmdxp[7]+1.5) < cell <= (hmdxp[7]+4.5) :
           Ag.append(1)
        elif (hmdxp[7]-1.5) <= cell <= (hmdxp[7]+1.5) :
           Ag.append(0)
        elif (hmdxp[7]-4.5) <= cell < (hmdxp[7]-1.5) :
           Ag.append(-1)
        elif (hmdxp[7]-7.5) <= cell < (hmdxp[7]-4.5) :
           Ag.append(-2)
        elif (hmdxp[7]-10.5) <= cell < (hmdxp[7]-7.5) :
           Ag.append(-3)
        else:
           Ag.append(-4)
St = []
for cell in humidex[:,8]:
        if (hmdxp[8]+10.5) < cell :
           St.append(4)
        elif (hmdxp[8]+7.5) < cell <= (hmdxp[8]+10.5) :
           St.append(3)
        elif (hmdxp[8]+4.5) < cell <= (hmdxp[8]+7.5) :
           St.append(2)
        elif (hmdxp[8]+1.5) < cell <= (hmdxp[8]+4.5) :
           St.append(1)
        elif (hmdxp[8]-1.5) <= cell <= (hmdxp[8]+1.5) :
           St.append(0)
        elif (hmdxp[8]-4.5) <= cell < (hmdxp[8]-1.5) :
           St.append(-1)
        elif (hmdxp[8]-7.5) <= cell < (hmdxp[8]-4.5) :
           St.append(-2)
        elif (hmdxp[8]-10.5) <= cell < (hmdxp[8]-7.5) :
           St.append(-3)
        else:
           St.append(-4)
Oc = []
for cell in humidex[:,9]:
        if (hmdxp[9]+10.5) < cell :
           Oc.append(4)
        elif (hmdxp[9]+7.5) < cell <= (hmdxp[9]+10.5) :
           Oc.append(3)
        elif (hmdxp[9]+4.5) < cell <= (hmdxp[9]+7.5) :
           Oc.append(2)
        elif (hmdxp[9]+1.5) < cell <= (hmdxp[9]+4.5) :
           Oc.append(1)
        elif (hmdxp[9]-1.5) <= cell <= (hmdxp[9]+1.5) :
           Oc.append(0)
        elif (hmdxp[9]-4.5) <= cell < (hmdxp[9]-1.5) :
           Oc.append(-1)
        elif (hmdxp[9]-7.5) <= cell < (hmdxp[9]-4.5) :
           Oc.append(-2)
        elif (hmdxp[9]-10.5) <= cell < (hmdxp[9]-7.5) :
           Oc.append(-3)
        else:
           Oc.append(-4)
Nv = []
for cell in humidex[:,10]:
        if (hmdxp[10]+10.5) < cell :
           Nv.append(4)
        elif (hmdxp[10]+7.5) < cell <= (hmdxp[10]+10.5) :
           Nv.append(3)
        elif (hmdxp[10]+4.5) < cell <= (hmdxp[10]+7.5) :
           Nv.append(2)
        elif (hmdxp[10]+1.5) < cell <= (hmdxp[10]+4.5) :
           Nv.append(1)
        elif (hmdxp[10]-1.5) <= cell <= (hmdxp[10]+1.5) :
           Nv.append(0)
        elif (hmdxp[10]-4.5) <= cell < (hmdxp[10]-1.5) :
           Nv.append(-1)
        elif (hmdxp[10]-7.5) <= cell < (hmdxp[10]-4.5) :
           Nv.append(-2)
        elif (hmdxp[10]-10.5) <= cell < (hmdxp[10]-7.5) :
           Nv.append(-3)
        else:
           Nv.append(-4)
Dc = []
for cell in humidex[:,11]:
        if (hmdxp[11]+10.5) < cell :
           Dc.append(4)
        elif (hmdxp[11]+7.5) < cell <= (hmdxp[11]+10.5) :
           Dc.append(3)
        elif (hmdxp[11]+4.5) < cell <= (hmdxp[11]+7.5) :
           Dc.append(2)
        elif (hmdxp[11]+1.5) < cell <= (hmdxp[11]+4.5) :
           Dc.append(1)
        elif (hmdxp[11]-1.5) <= cell <= (hmdxp[11]+1.5) :
           Dc.append(0)
        elif (hmdxp[11]-4.5) <= cell < (hmdxp[11]-1.5) :
           Dc.append(-1)
        elif (hmdxp[11]-7.5) <= cell < (hmdxp[11]-4.5) :
           Dc.append(-2)
        elif (hmdxp[11]-10.5) <= cell < (hmdxp[11]-7.5) :
           Dc.append(-3)
        else:
           Dc.append(-4)

cmgm = np.array([[En], [Fe], [Mz], [Ab], [My], [Jn], [Jl], [Ag], [St], [Oc], [Nv], [Dc]])
#print(cmgm.transpose())

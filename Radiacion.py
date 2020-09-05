#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 15:00:46 2019

@author: leo
"""

###############################################################################
######           Parte 1 - geometria solar
###############################################################################
import numpy as np

lat = int(input('Ingrese la latitud: '))
nj = int(input('Ingrese el día juliano: '))
hora = int(input('Ingrese la hora  del dia en valores decimales: '))
hrsol = int(input('Ingrese la cantidad de horas de sol: '))

print('Geometría solar para una latitud')

R = (np.pi/180)
Rad = (180/np.pi)

#lat = 19

#nj = 120

#hora = 14

dec = 23.45 * np.sin(( ( 360 * ( 284 + nj ) ) / 365) * R )

et= ((9.87*np.sin(R*((360*(nj-81)/384)))-(7.53*np.cos(R*(360*(nj-81)/384)))-(1.5*np.sin(R*(360*(nj-81)/384)))))/60

ang = (360*(12-(hora + et)))/24

alt = np.arcsin (((np.sin(R*dec) * np.sin(R*lat)) + (np.cos(R*dec)*np.cos(R*lat)*np.cos(R*ang)))) * Rad

#alt = np.arcsin (((np.sin(dec) * np.sin(lat)) + (np.cos(dec)*np.cos(lat)*np.cos(ang))))

aha = np.arccos((- (np.tan(R*dec) * np.tan(R*lat)))) * Rad

aha2 = np.arccos(- (np.tan(R*dec) * np.tan(R*lat))) * Rad

acm = np.arcsin(((np.cos(R*dec)*np.sin(R*ang))/np.cos(R*alt))) * Rad


print ('Declinacion =', dec, '°')
print ('Angulo horario =', ang, '°')
print ('Altura solar =', alt, '°')
print ('Angulo horario al amanecer =', aha, '°')
print ('Acimut =', acm, '°')


###############################################################################
######           Parte 2 - radiacion al tope de la atmosfera
###############################################################################

print ("Radiación en el tope de la atmosfera")

rext = np.abs((1/np.pi)*(1367*((np.cos(R*lat)*np.cos(R*dec)*np.sin(R*aha2))+(aha2*np.sin(R*lat)*np.sin(R*dec)))))

print ('Radiacion extraterrestre =', rext, 'W/m2')

###############################################################################
######           Parte 3-4 - radiación que llega a la superficie
###############################################################################

print ("Radiación que llega a la superficie")

#hrsol = 3

rg = np.abs(rext * ((0.29 * np.cos(R*lat))+(0.52*(hrsol/((2*aha)/15)))))

print ('Radiacion globar =', rg, 'W/m2')

#=I3*((0.29*COS(C2))+(0.52*(C11/((2*H6)/15))))
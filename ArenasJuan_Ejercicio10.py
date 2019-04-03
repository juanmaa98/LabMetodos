#!/usr/bin/env python
# coding: utf-8

# In[1]:


import urllib
from io import StringIO
from io import BytesIO
import csv
import numpy as np
from datetime import datetime
import matplotlib.pylab as plt
import pandas as pd
import scipy.signal as signal


# In[2]:


datos1=pd.read_csv('https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_1/Fourier/Datos/transacciones2008.txt',sep=";",decimal=",",header = None,names=["Fecha1", "Fecha2", "Valor", "Cantidad"])
datos2=pd.read_csv('https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_1/Fourier/Datos/transacciones2009.txt',sep=";",decimal=",",header = None,names=["Fecha1", "Fecha2", "Valor", "Cantidad"])
datos3=pd.read_csv('https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_1/Fourier/Datos/transacciones2010.txt',sep=";",decimal=",",header = None,names=["Fecha1", "Fecha2", "Valor", "Cantidad"])

datos=pd.concat([datos1,datos2,datos3],ignore_index=True)
datos=datos


# In[3]:


Fecha = datos["Fecha1"].str.split(" ", n = -1, expand = True)[0]
Hora = datos["Fecha2"].str.split(" ", n = -1, expand = True)[1]

Fecha=Fecha+' '+Hora


# In[4]:


datos.drop(columns =["Fecha1","Fecha2"], inplace = True) 
datos.insert(loc=0, column="Fecha", value=Fecha)


# In[5]:


datos["Fecha"]=pd.to_datetime(datos["Fecha"],format='%d/%m/%Y %H:%M:%S')
datos.set_index(["Fecha"],inplace=True)


# In[6]:


datos.to_csv(r'datos.csv')


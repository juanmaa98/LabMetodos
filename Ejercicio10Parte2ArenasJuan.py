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


datos=pd.read_csv('datos.csv')
datos.set_index(["Fecha"],inplace=True)

datos.drop(columns="Cantidad", inplace = True)


# In[3]:


datos.plot(figsize=(20,7))
plt.show()


# In[4]:


datos.reset_index(inplace=True)


# In[5]:


N  = 2    # Orden del filtro
Wn = 0.01 # Corte de frecuancia
B, A = signal.butter(N, Wn)
val=datos.values[:,1]
fecha=[datetime.strptime(x, "%Y-%m-%d %H:%M:%S") for x in datos.values[:,0]]


# In[6]:


datos_filt= signal.filtfilt(B,A, val)


# In[7]:


fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(211)
plt.plot(fecha,val, 'b-')
plt.plot(fecha,datos_filt, 'r-',linewidth=2)
plt.ylabel(r"Valor")
plt.legend(['Original','Filtrado'])
plt.title("Valor vs Fecha")
plt.show()


# In[ ]:


plt.figure(figsize=(20,7))
ruido=val-datos_filt
corr=signal.correlate(ruido,ruido,mode="full")
plt.plot(corr[len(corr)//2:])
plt.show()


# In[ ]:


N2  = 3    # Orden del filtro
Wn2 = 0.0001 # Corte de frecuancia
B2, A2 = signal.butter(N2, Wn2)

datos_filt2= signal.filtfilt(B2,A2, val)

fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(211)
plt.plot(fecha,val, 'b-')
plt.plot(fecha,datos_filt2, 'r-',linewidth=2)
plt.ylabel(r"Valor")
plt.legend(['Original','Filtrado'])
plt.title("Valor vs Fecha")
plt.show()


# In[ ]:


plt.figure(figsize=(20,7))
ruido2=val-datos_filt2
corr2=signal.correlate(ruido2,ruido2,mode="full")
plt.plot(corr2[len(corr2)//2:])
plt.show()


# In[ ]:


N3  = 1    # Orden del filtro
Wn3 = 0.00003 # Corte de frecuencia
B3, A3 = signal.butter(N3, Wn3)

datos_filt3= signal.filtfilt(B3,A3, val)

fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(211)
plt.plot(fecha,val, 'b-')
plt.plot(fecha,datos_filt3, 'r-',linewidth=2)
plt.ylabel(r"Valor")
plt.legend(['Original','Filtrado'])
plt.title("Valor vs Fecha")
plt.show()


# In[ ]:


plt.figure(figsize=(20,7))
ruido3=val-datos_filt3
corr3=signal.correlate(ruido3,ruido3,mode="full")
plt.plot(corr3[len(corr3)//2:])
plt.show()


# In[ ]:


N4  = 2    # Orden del filtro
Wn4 = 0.00003 # Corte de frecuencia
B4, A4 = signal.butter(N4, Wn4)

datos_filt4= signal.filtfilt(B4,A4, val)

fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(211)
plt.plot(fecha,val, 'b-')
plt.plot(fecha,datos_filt4, 'r-',linewidth=2)
plt.ylabel(r"Valor")
plt.legend(['Original','Filtrado'])
plt.title("Valor vs Fecha")
plt.show()


# In[ ]:


plt.figure(figsize=(20,7))
ruido4=val-datos_filt4
corr4=signal.correlate(ruido4,ruido4,mode="full")
plt.plot(corr4[len(corr4)//2:])
plt.show()


# In[ ]:


N5  = 2    # Orden del filtro
Wn5 = 0.00006 # Corte de frecuencia
B5, A5 = signal.butter(N, Wn)

datos_filt5= signal.filtfilt(B5,A5, val)

fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(211)
plt.plot(fecha,val, 'b-')
plt.plot(fecha,datos_filt5, 'r-',linewidth=2)
plt.ylabel(r"Valor")
plt.legend(['Original','Filtrado'])
plt.title("Valor vs Fecha")
plt.show()
print('estos valores funcionan mejor: N=2, Wn=0.00006')


# In[ ]:


plt.figure(figsize=(20,7))
ruido5=val-datos_filt5
corr5=signal.correlate(ruido5,ruido5,mode="full")
plt.plot(corr5[len(corr5)//2:])
plt.show()


# In[ ]:





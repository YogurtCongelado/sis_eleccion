# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 01:45:48 2020

@author: yogurtcongelado
"""

from numpy import random
from collections import Counter
import statistics
import numpy as np

lista_votos = []

resultados_FPP = []

preferencias = [0,0,0,0]

resultados_PV = []

tota_p = []
total_c1 = []
total_c2 = []
total_c3 = []
total_c4 = []

preferencias_iteradas = []


th = 4

def forma_de_conteo_1(n):
    preferencias_iteradas = []
    for i in range(n):
        x=random.randint(1,10, size=(4))
        
        suma = list(map(sum, zip(x, preferencias)))
        
        gi = {'Cand1': x[0], 'Cand2': x[1], 'Cand3':x[2], 'Cand4': x[3]}
        
        ganador = max(gi, key=gi.get)
        
        preferencias_iteradas.append(suma)
        
        #print(x)
        #print(ganador)
        
        lista_votos.append(ganador)
        #print(preferencias_iteradas)
        
    resultado_preferencias = list() 
    for j in range(0, len(preferencias_iteradas[0])): 
        tmp = 0
        for i in range(0, len(preferencias_iteradas)): 
            tmp = tmp + preferencias_iteradas[i][j] 
        resultado_preferencias.append(tmp)   
        
        
    #print(resultado_preferencias)
    gf= Counter(lista_votos)
    ganador_conteo = max(gf, key=gf.get)
    #print(ganador_conteo)

    gustospreferencias=  [i / (10*n) for i in resultado_preferencias]
    total_c1.append(gustospreferencias[0])
    total_c2.append(gustospreferencias[1])
    total_c3.append(gustospreferencias[2])
    total_c4.append(gustospreferencias[3])
    
    #print(total_c1)
    #print(gustospreferencias)
    gprom = {'Cand1': gustospreferencias[0], 'Cand2': gustospreferencias[1], 
             'Cand3':gustospreferencias[2], 'Cand4': gustospreferencias[3]}
    ganador_promedio = max(gprom, key=gprom.get) 
    #print(ganador_promedio)     
    #print(gprom)
    resultados_PV.append(ganador_promedio)
    resultados_FPP.append(ganador_conteo)
    
    
    #desv_est_med1 = statistics.stdev(total_c1)/np.sqrt(n)
    #desv_est_med2 = statistics.stdev(total_c2)/np.sqrt(n)
    #desv_est_med3 = statistics.stdev(total_c3)/np.sqrt(n)
    #desv_est_med4 = statistics.stdev(total_c4)/np.sqrt(n)
    
    
    
#forma_de_conteo_1(100)

def votaciones_totales(n,m):
    for i in range(m):
        forma_de_conteo_1(n)
    total_c1.append(5)
    total_c2.append(5)
    total_c3.append(5)
    total_c4.append(5)
    
    print("Los resultados PV fueron:", "\n" , "\n" , 
          "Cand1:",resultados_PV.count('Cand1')  , "\n" , 
          "Cand2:",resultados_PV.count('Cand2') , "\n" , 
          "Cand3:",resultados_PV.count('Cand3') , "\n" , 
          "Cand4:",resultados_PV.count('Cand4') , "\n"  
                        )
    print("Los resultados FPP fueron:", "\n" , "\n" , 
          "Cand1:",resultados_FPP.count('Cand1') , "\n" , 
          "Cand2:",resultados_FPP.count('Cand2') , "\n" , 
          "Cand3:",resultados_FPP.count('Cand3') , "\n" , 
          "Cand4:",resultados_FPP.count('Cand4') , "\n"  

              )

    print("La afinidad media fue:","\n" , "Cand1:", statistics.mean(total_c1) 
          , u"\u00B1" , (statistics.stdev(total_c1)/np.sqrt(n))
          ,"\n" , "Cand2:", statistics.mean(total_c2) , u"\u00B1" ,
          (statistics.stdev(total_c2)/np.sqrt(n))
          ,"\n" , "Cand3:", statistics.mean(total_c3), u"\u00B1" ,
          statistics.stdev(total_c3)/np.sqrt(n)
          ,"\n" , "Cand4:", (statistics.mean(total_c4)) , u"\u00B1",
          (statistics.stdev(total_c4)/np.sqrt(n))
          )
votaciones_totales(1700, 10)
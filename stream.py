# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 14:24:49 2020

@author: Martinez Garcia Isabel y Luna Ganzáles Rocio
"""

import json
Probabilidades = False

with open("estadis.json","r") as read_file:
	data = json.load(read_file)
	Probabilidades = data['probabilidades']

archivo = open('tweet.txt','r') 
mensaje = archivo.read()
mensaje = mensaje.split()
print(mensaje)
archivo.close()

def stream(CON):
	num = 0
	op = 0.0
	if not CON:
		return " El tweet No es Stream"
	while num<len(CON):
		op = op + float(CON[num][1])
		num = num + 1
	op = op /len(CON)
	return stream1(op)

def stream1(op):
	print("El Promedio =",op)
	if op>=0.55:
		return "El tweet es Stream"
	else:
		return "El tweet No es Stream"
    
def esta(mensaje,Probabilidades):
	i=0
	CON=[]
	while i<len(mensaje):
		j=0
		while j<len(Probabilidades):
			if mensaje[i]==Probabilidades[j][0]:
				P=Probabilidades[i]
				CON=CON+[P]
			j=j+1
		i=i+1
	return stream(CON)
print(esta(mensaje,Probabilidades))
#el tweet es Stream Vamos seguirle Bloodborne, Vamos a darle al among us
#el tweet  no es Stream pedo wey, Vamos darle nueva temporada FALL GUYS
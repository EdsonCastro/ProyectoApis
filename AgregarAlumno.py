#!/usr/bin/python
# -*- coding: utf-8 -*-    

#Agrega el Alumno a la cadena de caracteres, concatena y guarda la cadena concatenada en el fichero.
def agregaralumnonota(nombre, nota, estado):
    f = open('outputNotas.json','r')
    cadena = f.read()
    f.close()
    #nombre = 'Mario'
    #nota = '8'
    #estado ='Notable'
    conca = ', {"Nombre": "'+nombre+'", "Nota": "'+nota+'", "Estado": "'+estado+'"}'
    cadena = cadena[:(len(cadena)-2)]+conca+cadena[(len(cadena)-2):]
    #print cadena, len(cadena)        
    f = open('outputNotas.json','w')
    f.write(cadena)
    f.close()
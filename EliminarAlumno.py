#!/usr/bin/python
# -*- coding: utf-8 -*-    

#Elimina el primer alumno con ese nombre de la lista
def eliminarAlumno(nombre):
    f = open('outputNotas.json','r')
    cadena = f.read()
    #nombre = 'Mario'
    #nota = '8'
    #estado ='Notable'
    #conca = ', {"Nombre": "'+nombre+'", "Nota": "'+nota+'", "Estado": "'+estado+'"}'
    #print cadena
    #cadena = cadena[:(len(cadena)-2)]+conca+cadena[(len(cadena)-2):]
    #print cadena, len(cadena)        
    f.close()    
    msj = 'Alumno no encontrado'    
    if nombre in cadena:
        n = len(nombre)
        indice = 0    
        while indice < len(cadena):
            if cadena[indice] == nombre[0]:
                i = 0
                conta = 0
                while i < n:                
                    if cadena[indice+i] == nombre[i]:    #Cuenta si el nombre encontrado tiene la misma longitud 
                        conta += 1                       #que el buscado, ya que puede que busque a Juana habiendo Juan.
                    i += 1
                if n == conta:                           #Compara si la longitud del nombre es igual que el nombre encontrado.
                    j = indice
                    borraratras=0
                    while cadena[j] != '}':                    #Calcula los datos del alumno que se van a borrar.
                        #print cadena[j]
                        borraratras += 1
                        j += 1                
                    if cadena[indice+borraratras+1] == ']':    #Si es el ultimo.
                        borraratras = borraratras+1
                        borraradelante = 14                    
                    elif cadena[indice-13] == '[':
                        borraratras = borraratras+3            #Si es el primero.
                        borraradelante = 12
                    else:
                        borraratras = borraratras+2            #Si esta en medio.
                        borraradelante = 13
                    cadena = cadena[:(indice-borraradelante)]+cadena[indice+borraratras:]
                    msj = 'Alumno encontardo y eliminado correctaemte'                    
                    indice = len(cadena)
            indice += 1
    #print msj
    f = open('outputNotas.json','w')
    f.write(cadena)
    f.close()
    return msj

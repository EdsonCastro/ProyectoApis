#!/usr/bin/python
# -*- coding: utf-8 -*- 

from SperadsheetToJSON import *
from AgregarAlumno import *
from EliminarAlumno import *
from FiletoDropbox import *
import io
import os                         #para redireccionar la url
import json
from flask import request
from flask import Flask, render_template, redirect
from crypt import crypt

app = Flask(__name__)

#Cdigo que redireccionaria iniciando session y mostrando el google calendar.
@app.route("/vermygooglecalendar", methods=['POST'])
def vermygooglecalendar():
    
    return render_template('tareas.html')

#Codigo que redireccionaria a twitter.
@app.route("/vermytwitter", methods=['POST'])
def vermytwitter():    
    return redirect("https://twitter.com/Proyecto_Apis",code=302)

#Muestra la Hoja de calculo de las notas.
@app.route("/vernotasgoogle", methods=['POST'])
def vernotasgogle():    
    return redirect("https://docs.google.com/spreadsheets/d/1FMVP1auyd-8cTj0QIOElNZ0CB_FATzNnYxvJJmOt4_I/pubhtml",code=302)

#Genera el html de las notas en un una tabla y la muestra.
@app.route("/vernotas", methods=['POST'])
def vernotas():    
    generarTabla()
    return render_template('tabla.html')

#Agrega un Alumno con sus datos al archivo JSON y lo sube a Dropbox.
@app.route("/agregarnotaalumno", methods=['POST'])
def agregarnotaalumno():
    alumno = request.form['alumno']
    nota   = request.form['nota'] 
    estado = request.form['estado']
    agregaralumnonota(alumno, nota, estado)
    actulizarNotasDropbox()
    return render_template('notasexamen.html')

#Elimina el Alumno de el archivo JSON y lo sube al Dropbox.
#La busqueda es por la primera coincidencia del nombre, importan las mayusculas.
@app.route("/eliminarnotaalumno", methods=['POST'])
def eliminarnotaalumno():
    nombre = request.form['alumno']
    print nombre
    print eliminarAlumno(nombre)
    generarTabla()
    actulizarNotasDropbox()    
    return render_template('notasexamen.html')

@app.route("/publicarnotasexamen", methods=['POST'])
def publicarnotasexamen():
    actulizarNotasDropbox()
    return render_template('notasexamen.html')

@app.route("/publicarfechaexamen", methods=['POST'])
def publicarfechaexamen():
    #aca iria el codigo para hacer el twitt y postearlo y agregar a google calendar    
    return render_template('fechaexamen.html')

@app.route("/formularionotasexamen", methods=['POST'])
def formularionotasexamen():
    #googletoTabla()
    return render_template('notasexamen.html')

@app.route("/formulariofechaexamen", methods=['POST'])
def formulariofechaexamen():
    return render_template('fechaexamen.html')

@app.route("/tareas", methods=['POST'])
def tareas():
    return render_template('tareas.html')

@app.route("/salir", methods=['POST'])
def salir():
    htpuser = ''
    htpasswd = ''
    authdU = crypt('wrongpw',htpuser)==htpuser
    authdP = crypt('wrongpw',htpasswd)==htpasswd
    return render_template('index.html')

@app.route("/buscar", methods=['POST'])
def buscar():
    user = request.form['text']
    pw   = request.form['passwd'] 
    htpuser = 'Jywn1PBEdYjkg'
    htpasswd = 'Jywn1PBEdYjkg'
    authU = crypt(pw,htpasswd)==htpasswd
    authP = crypt(user,htpuser)==htpuser
    #print authU, authP
    if (authU == True) and (authP == True):        
        return render_template('tareas.html')
    else:        
        return render_template('index.html')

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=False)
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)    
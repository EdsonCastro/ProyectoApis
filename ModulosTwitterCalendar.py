#!/usr/bin/python
# -*- coding: utf-8 -*-

from login import *
from flask import request
from flask import Flask,render_template


#---------------------------------------------------------------TWITTER--------------------------------------------------------------
twitt = login_twitter()
url = 'https://docs.google.com/spreadsheets/d/1FMVP1auyd-8cTj0QIOElNZ0CB_FATzNnYxvJJmOt4_I/pubhtml'

def vermytwitter():
    stats = twitt.home_timeline(count = 5)
    for tweet in stats:
	    print tweet.text+'\n'

def publicarnotasexamen():
    try:
	    twitt.update_status(status = 'Publicada las notas del examen '+url)
    except:
		print 'Tweet ya publicado.'

def publicarfechaexamen():
    try:
        hinicio = request.form['hinicio'] #yyyy-mm-ddThh:mm:ss
        hfin =  request.form['hfin']     #yyyy-mm-ddThh:mm:ss
        aula = request.form['aula']
        examencalendar(aula,hinicio,hfin)
        twitt.update_status(status = 'Publicado examen en google calendar')
	except:
	    print 'Tweet ya publicado.'

def eliminarultimotweet():
	stats = twitt.user_timeline(count = 1)
	eliminartweets(stats)
	
def eliminartweets(stats):
	for tweet in stats:
	    twitt.destroy_status(tweet.id)
		
#-----------------------------------------------------------GOOGLE_CALENDAR-----------------------------------------------------------
service = login_calendar()

def vermygooglecalendar():
    eventsResult = service.events().list(
        calendarId='primary', maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])
   
    if not events:
        print 'Eventos recientes no encontrados.'
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print start, event['summary']

def examencalendar(aula,hinicio,hfin):
    evento = {
	    'summary': 'EXAMEN',
        'location': aula,
        'start': {
            'dateTime': hinicio,
            'timeZone': 'Europe/Madrid'
        },
        'end': {
            'dateTime': hfin,
            'timeZone': 'Europe/Madrid'
        },
    }
    service.events().insert(calendarId='primary', body=evento).execute()
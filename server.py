

from bs4 import BeautifulSoup
import requests
import RPi.GPIO as GPIO
import threading 
import drivers 
from time import sleep
from flask import Flask, render_template
app = Flask(__name__)
display = drivers.Lcd()

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/bitcoin/')
def Interrupcion():
  url = "https://mx.investing.com/crypto/bitcoin/btc-mxn"
  r  = requests.get(url)
  data = r.text
  soup = BeautifulSoup(data, 'lxml')
  temp = soup.find_all('span', class_='text-2xl')
  precio    = list()
       
  for i in temp:
     precio.append(i.text)
  display.lcd_clear()
  display.lcd_display_string("Bitcoin a pesos:", 1)
  display.lcd_display_string(i.text,2)
  return i.text
  
@app.route('/dolar/')
def Interrupcion2():
  urldol = 'https://mx.investing.com/currencies/usd-mxn'
  rdol  = requests.get(urldol)
  datadol = rdol.text
  soupdol = BeautifulSoup(datadol, 'lxml')
  tempdol = soupdol.find_all('span', class_='text-2xl')
  preciodol    = list()
       
  for j in tempdol:
     preciodol.append(j.text)
  display.lcd_clear()
  display.lcd_display_string("dolar a pesos:", 1)
  display.lcd_display_string(j.text,2)
  return j.text


@app.route('/euro/')
def Interrupcion3():
  url3 = "https://mx.investing.com/currencies/eur-mxn"
  r3  = requests.get(url3)
  data3 = r3.text
  soup3 = BeautifulSoup(data3, 'lxml')
  temp3 = soup3.find_all('span', class_='text-2xl')
  precio3   = list()
       
  for l in temp3:
     precio3.append(l.text)
  display.lcd_clear()
  display.lcd_display_string("euro a pesos:", 1)
  display.lcd_display_string(l.text,2)
  return l.text

@app.route('/yen/')
def Interrupcion4():
  url4 = "https://mx.investing.com/currencies/jpy-mxn"
  r4  = requests.get(url4)
  data4 = r4.text
  soup4 = BeautifulSoup(data4, 'lxml')
  temp4 = soup4.find_all('span', class_='text-2xl')
  precio4    = list()
       
  for i4 in temp4:
     precio4.append(i4.text)
  display.lcd_clear()
  display.lcd_display_string("yenes a pesos:", 1)
  display.lcd_display_string(i4.text,2)
  return i4.text

@app.route('/parg/')
def Interrupcion5():
  url5 = "https://mx.investing.com/currencies/ars-mxn"
  r5  = requests.get(url5)
  data5 = r5.text
  soup5 = BeautifulSoup(data5, 'lxml')
  temp = soup5.find_all('span', class_='text-2xl')
  precio5    = list()
       
  for i5 in temp:
     precio5.append(i5.text)
  display.lcd_clear()
  display.lcd_display_string("ARS a MXN:", 1)
  display.lcd_display_string(i5.text,2)
  return i5.text

if __name__ == '__main__':
  app.run(debug=True)

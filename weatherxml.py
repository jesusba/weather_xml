# -*- coding: utf-8 -*-
import requests
from lxml import etree
from jinja2 import Template
import webbrowser

f = open('plantilla.xml','r')

tree = etree.parse('plantilla.xml')
raiz = etree.fromstring(plantilla_as_string)

xml = ' '

for linea in f:
	xml += linea

plantilla = Template(xtml)

ciudades = ["Almeria","Cadiz","Cordoba","Granada","Huelva","Jaen","Malaga","Sevilla","Dos Hermanas"]

for ciudadp in ciudades:
	valores = {'q': '%s' % ciudadp,'mode': 'xml','unit': 'metric','lang': 'es'}
	respuesta = requests.get('http://api.openweathermap.org/data/2.5/weather',params=valores)
	
print(respuesta.url)

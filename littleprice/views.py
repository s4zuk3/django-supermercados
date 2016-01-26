#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from django.shortcuts import render_to_response

#login_user (0 o 1), se utiliza para definir las opciones del panel a mostrar.
def index_view(request):
	login_user = 1
	return render_to_response('web/index.html',locals())


#login_user (0 o 1), se utiliza para definir las opciones del panel a mostrar. Aunque se supone que en esta vista solo se puede entrar si estas logeado
#indice_supermercados, es un diccionario de nombre del supermercado y el indice.
#super_name es la tupla que se le envia al template
def supermercados_view(request):
	login_user = 1
	indice_supermercados = { 'Tottus':3,'Lider':6,'Ekono':1}
	super_name = indice_supermercados.items()
	return render_to_response('web/supermercados.html', locals()  )

#login_user (0 o 1), se utiliza para definir las opciones del panel a mostrar.
#lista_comunas, una lista con todos las comunas posibles.
def myaccount_view(request):
	login_user = 1
	lista_comunas = ['Estación Central','Puente Alto','Maipu','Pudahuel']
	return render_to_response('web/myaccount.html',locals())



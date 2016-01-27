#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from django.shortcuts import render_to_response

#login_user (0 o 1), se utiliza para definir las opciones del panel a mostrar. aca puede ser 0 o 1
def index_view(request):
	login_user = 1
	return render_to_response('web/index.html',locals())


# login_user 1, se supone que en esta vista solo se puede entrar si estas logeado
#indice_supermercados, es un diccionario de nombre del supermercado y el indice.
#super_name es la tupla que se le envia al template
def supermercados_view(request):
	login_user = 1
	indice_supermercados = { 'Tottus':3,'Lider':6,'Ekono':1}
	super_name = indice_supermercados.items()
	return render_to_response('web/supermercados.html', locals()  )

#login_user 1, se supone que si esta en esta vista es porque esta logeado
#lista_comunas, una lista con todos las comunas posibles.
# datos del usuario para mostrar como relleno de los campos.
def myaccount_view(request):
	login_user = 1
	id_usuario = 'MiJanitoxForte556'
	email_usuario = 'ezzejanox556@delflow.com'
	nombre_usuario = 'Juan'
	apellido_usuario = 'Del rio'
	comuna_usuario = 'Puente Alto'
	lista_comunas = ['Estación Central','Puente Alto','Maipu','Pudahuel']
	return render_to_response('web/myaccount.html',locals())

#login_user 0, se supone que el user no deberia estar aca si ya esta logeado xd
def login_view(request):
	login_user = 0
	return render_to_response('web/login.html',locals())

#login_user 0, se supone que el user no deberia estar aca si ya esta logeado xd
def registro_view(request):
	login_user = 0
	return render_to_response('web/registro.html',locals())


#vista comun al seleccionar un producto de canasta basica
#da lo mismo que login user, todos pueden ver esta
#definir name_title y el diccionario con el producto relacionado que llamo a esta vista
def canasta_basica_view(request):
	login_user = 0
	
	name_title = Arroz
	diccionario_productos = { 'Acuenta':357,'Campo Lindo':451,'Sabanero':555}
	marca_precio = diccionario_productos.items()
	

	return render_to_response('web/canasta_basica.html',locals())

#login_user 1, solo puede estar aca si esta logeado
def mis_productos_view(request):
	login_user = 1
	return render_to_response('web/mis_productos.html',locals())

	#login_user 1, solo puede estar aca si esta logeado
def favoritos_view(request):
	login_user = 1
	return render_to_response('web/favoritos.html',locals())

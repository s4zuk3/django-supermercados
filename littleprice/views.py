#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from django.shortcuts import render_to_response


def index_view(request):
	login_user = 1
	return render_to_response('web/index.html',locals())

def supermercados_view(request):
	login_user = 1
	section_one_name = "Supermercados en tu comuna"
	section_two_name = "Ubicación en el mapa"
	indice_supermercados = { 'Tottus':3,'Lider':6,'Ekono':1}
	super_name = indice_supermercados.items()

	return render_to_response('web/supermercados.html', locals()  )



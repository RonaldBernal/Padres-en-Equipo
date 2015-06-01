# coding=utf8
# -*- coding: utf8 -*-
from django.shortcuts import render

def landing(request):
	return render(request, 'landing.html', {"title": "Padres en Equipo"})

def Embarazo(request):
	return render(request, 'embarazo.html', {"title": "Embarazo"})

def E1(request):
	return render(request, 'E1.html', {"title": "¡Cuidado Madres Primerizas!"})

def E2(request):
	return render(request, 'E2.html', {"title": "Ejercicio en mi Embarazo"})

def E3(request):
	return render(request, 'E3.html', {"title": "Después de nacer"})
	
def E4(request):
	return render(request, 'E4.html', {"title": "De regreso a la línea"})

def Nutricion(request):
	return render(request, 'nutricion.html', {"title": "Nutrición"})

def N1(request):
	return render(request, 'N1.html', {"title": "Comiendo Juntos"})
	
def N2(request):
	return render(request, 'N2.html', {"title": "Alimentando a mi Bebé"})

def Cuidados(request):
	return render(request, 'cuidados.html', {"title": "Cuidados e Higiene"})
	
def CH1(request):
	return render(request, 'CH1.html', {"title": "La pérdida del cordón umbilical"})
	
def CH2(request):
	return render(request, 'CH2.html', {"title": "¿Qué hacer cuando el bebé tiene flatulencias?"})

def Papa(request):
	return render(request, 'papa.html', {"title": "Para Papá"})

def PP1(request):
	return render(request, 'PP1.html', {"title": "Qué hacer si su hijo miente?"})
	
def PP2(request):
	return render(request, 'PP2.html', {"title": "La buena disciplina, un padre responsable."})

def Vestimenta(request):
	return render(request, 'vestimenta.html', {"title": "Vestimenta"})

def V1(request):
	return render(request, 'V1.html', {"title": "¿Qué tipo de ropa debe utilizar tu bebé?"})

def Juegos(request):
	return render(request, 'juegos.html', {"title": "Juegos para padres e hijos"})

def G1(request):
	return render(request, 'G1.html', {"title": "¡Los cuentos toman vida!"})
	
def G2(request):
	return render(request, 'G2.html', {"title": "Tu pequeño artista"})

def G3(request):
	return render(request, 'G3.html', {"title": "¡3, 2, 1 Música maestro!"})

def apps(request):
	return render(request, 'apps.html', {"title": "Aplicaciones para el celular de mamá y papá"})

from django.shortcuts import render

def landing(request):
	return render(request, 'landing.html', {"title": "Padres en Equipo"})

def detail(request):
	return render(request, 'detail.html', {})


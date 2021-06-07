from django import http
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from .models import Participante
from .models import Conferencista

def index(request):
    return render(request, 'registro/index.html')

def participantes(request):
    

    if request.method == 'POST':
        #Aqui viene la info del formulario
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        twitter = request.POST.get('twitter')

        p = Participante(nombre=nombre, apellido=apellido, correo=correo, twitter=twitter)
        p.save()

        messages.add_message(request, messages.INFO, f'El participante {nombre} {apellido} ha sido registrado con éxito')

    #Metodo GET
    q = request.GET.get('q')

    if q:
        data = Participante.objects.filter(nombre__startswith=q).order_by('nombre') #buscar por nombre
    else:
        data = Participante.objects.all().order_by('nombre') #'-nombre' para ordenar descendednte nos regresa todos los registros que tiene participante

    ctx = {
        'participantes': data,
        'q': q
    }

    return render(request, 'registro/participantes.html', ctx) #recibe minimo 2 parametros

def conferencistas(request):
    

    if request.method == 'POST':
        #Aqui viene la info del formulario
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        experiencia = request.POST.get('experiencia')

        c = Conferencista(nombre=nombre, apellido=apellido, experiencia=experiencia)
        c.save()

        messages.add_message(request, messages.INFO,  f'El conferencista {nombre} {apellido} ha sido registrado con éxito')

    #Metodo GET
    q = request.GET.get('q')

    if q:
        data = Conferencista.objects.filter(nombre__startswith=q).order_by('nombre') #buscar por nombre
    else:
        data = Conferencista.objects.all().order_by('nombre') #'-nombre' para ordenar descendednte nos regresa todos los registros que tiene participante

    ctx = {
        'conferencistas': data,
        'q': q
    }

    return render(request, 'registro/conferencistas.html', ctx) #recibe minimo 2 parametros
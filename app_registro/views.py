from django import http
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.urls import reverse
from .models import Participante
from .models import Conferencista

from telegram import Bot

TOKEN = '1834248388:AAHxb3lx6mY4lK6qnrtYhE_zhoz8Cy65Z-Y'
GROUP_ID = -510768242 #Identifica el grupo de telegram

bot = Bot(token=TOKEN)

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

        msj = f'El participante {nombre} {apellido} ha sido registrado con éxito'

        #codigos para enviar mensaje a grupo de telegram
        try:
            bot.send_message(chat_id=GROUP_ID, text=msj)
        except Exception as e:
            msj += f'<br/><strong>{e}</strong>'

        messages.add_message(request, messages.INFO, msj)
    #Metodo GET
    activo = 'participantes'

    q = request.GET.get('q')

    if q:
        data = Participante.objects.filter(nombre__startswith=q).order_by('nombre') #buscar por nombre
    else:
        data = Participante.objects.all().order_by('nombre') #'-nombre' para ordenar descendednte nos regresa todos los registros que tiene participante

    ctx = {
        'participantes': data,
        'q': q,
        'activo': activo
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
    activo = 'conferencistas'

    q = request.GET.get('q')

    if q:
        data = Conferencista.objects.filter(nombre__startswith=q).order_by('nombre') #buscar por nombre
    else:
        data = Conferencista.objects.all().order_by('nombre') #'-nombre' para ordenar descendednte nos regresa todos los registros que tiene participante

    ctx = {
        'conferencistas': data,
        'q': q,
        'activo': activo
    }

    return render(request, 'registro/conferencistas.html', ctx) #recibe minimo 2 parametros

def eliminar_participante(request, id):
    Participante.objects.get(pk=id).delete() #get solo se retorna un solo objeto
    return redirect(reverse('participantes'))

def editar_participante(request, id):
    # par = Participante.objects.get(pk=id)
    par = get_object_or_404(Participante, pk=id)

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        twitter = request.POST.get('twitter')

        par.nombre = nombre
        par.apellido = apellido
        par.correo = correo
        par.twitter = twitter
        
        par.save()

    data = Participante.objects.all().order_by('nombre') 
    
    ctx = {
        'activo':'participantes',
        'participantes': data,
        'p': par
    }

    return render(request, 'registro/participantes.html', ctx) #recibe minimo 2 parametros

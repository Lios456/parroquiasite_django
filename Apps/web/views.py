from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.

def index(request):
    context = {
        'noticias': Noticia.objects.all().order_by('-fecha')[:4]
    }
    return render(request, 'index.html', context)

def cambio(request):
    return render(request, 'cambiofiesta.html')

def about(request):
    return render(request, 'about.php')

def news(request):
    context = {
        'noticias': Noticia.objects.all().order_by('-fecha')
    }
    if request.method == 'POST':
        try:
            n = Noticia()
            n.titulo = request.POST.get('titulo')
            n.contenido = request.POST.get('detalle')
            n.autor = request.user
            n.save()
            messages.success(request,'Se ha registrado con éxito la noticia')
            return redirect('/news/')
        except Exception as e:
            messages.error(request, f'Error:{e}')
    return render(request, 'noticias.php', context)

def new(request,id):
    context = {
        'noticia':Noticia.objects.get(id=id)
    }
    return render(request, 'noticia.html', context)

def edit_news(request, id):
    noti = Noticia.objects.get(id=id)
    context = {
        'noticias': Noticia.objects.all(),
        'n': noti
    }
    if request.method == 'POST':
        try:
            noti.titulo = request.POST.get('titulo')
            noti.contenido = request.POST.get('detalle')
            noti.save()
            messages.success(request,'Se ha editado con éxito la noticia')
            return redirect('/news/')

        except Exception as e:
            messages.error(request, f'Error:{e}')
    return render(request, 'noticias.php', context)

def catequesis(request):
    return render(request, 'catequesis.php')

def santisimacruz(request):
    return render(request, 'santisimacruz.php')

def santisimatrinidad(request):
    return render(request, 'santisimatrinidad.php')



def contacto(request):
    if request.method == 'POST':
        try:
            m = Mensaje()
            m.name =  request.POST.get('name')
            m.email = request.POST.get('email')
            m.phone = request.POST.get('phone')
            m.address =request.POST.get('address')
            m.message =request.POST.get('message')
            m.save()
            messages.success(request,'Se ha enviado con éxito el mensaje')

        except Exception as e:
            messages.error(request, f'Error:{e}')
    
    return render(request, 'contacto.php')
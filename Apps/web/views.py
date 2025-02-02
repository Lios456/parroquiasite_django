from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.core.mail import send_mail
from django.contrib.auth import login, logout, authenticate
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    context = {
        'noticias': Noticia.objects.all().order_by('-fecha')[:4]
    }
    return render(request, 'index.html', context)

def cambio(request):
    return render(request, 'cambiofiesta.html')

def about(request):
    return render(request, 'about.html')

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
    return render(request, 'noticias.html', context)

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
    return render(request, 'noticias.html', context)


def santisimacruz(request):
    return render(request, 'santisimacruz.html')

def santisimatrinidad(request):
    return render(request, 'santisimatrinidad.html')


def contacto(request):
    if request.method == 'POST':
        try:
            # Obtener datos del formulario
            name = request.POST.get('name')
            email = request.POST.get('email')  # Email del usuario
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            message = request.POST.get('message')

            # Guardar en la base de datos
            m = Mensaje(
                name=name,
                email=email,
                phone=phone,
                address=address,
                message=message,
            )
            m.save()

            # 📧 Enviar correo al usuario
            subject_user = "Confirmación de tu mensaje"
            body_user = f"""
            Hola {name},

            Hemos recibido tu mensaje y nos pondremos en contacto contigo lo antes posible.

            Detalles de tu mensaje:
            -----------------------
            Nombre: {name}
            Email: {email}
            Teléfono: {phone}
            Dirección: {address}
            Mensaje: {message}

            Gracias por contactarnos.

            Atentamente,
            Santísima Trinidad La Laguna
            """

            send_mail(
                subject_user,
                body_user,
                'santisimatrinidadlalaguna@gmail.com',  # Remitente
                [email],  # Destinatario: usuario que llenó el formulario
                fail_silently=False,
            )

            # 📧 Enviar correo a la empresa
            subject_admin = f"Nuevo mensaje de {name}"
            body_admin = f"""
            ¡Hola!

            {name} se ha puesto en contacto contigo a través del formulario.

            Detalles del mensaje:
            -----------------------
            Nombre: {name}
            Email: {email}
            Teléfono: {phone}
            Dirección: {address}
            Mensaje: {message}

            Por favor, revisa y responde lo antes posible.

            Atentamente,
            Sistema de Contacto
            """

            send_mail(
                subject_admin,
                body_admin,
                'santisimatrinidadlalaguna@gmail.com',  # Remitente
                ['santisimatrinidadlalaguna@gmail.com'],  # Destinatario: correo de la empresa
                fail_silently=False,
            )

            messages.success(request, 'Tu mensaje ha sido enviado con éxito. Revisa tu correo.')

        except Exception as e:
            messages.error(request, f'Error al enviar el mensaje: {str(e)}')

    return render(request, 'contacto.html')


def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            #Autenticar
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Bienvenido {user}')
                return redirect('/news/')
            else:
                messages.error(request, f"Credenciales incorrectas")
                return render(request, 'login.html', context)
        except Exception as e:
            messages.error(request, f"Error al iniciar sesión: {e}")
            return render(request, 'login.html', context)

    else:
        return render(request, 'login.html', context)
    
def logout_view(request):
    try:
        messages.success(request, f'Adiós {request.user}')
        logout(request)
        
        return redirect('/login/')
    except Exception as e:
        messages.error(request, f"Error al cerrar sesión: {e}")
        return render(request, 'login.html')
    
def mensajes(request):
    mensajes = Mensaje.objects.all().order_by('-id') 
    paginator = Paginator(mensajes, 5) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'mensajes.html', {'page_obj': page_obj})

def eliminar_mensaje(request, id):
    if request.method == 'POST':
        mensaje = Mensaje.objects.get(id=id)
        try:
            mensaje.delete()
            messages.success(request, f'Mensaje eliminado')
            return redirect('/mensajes/')
        except Exception as e:
            messages.error(request, f"Error al eliminar el mensaje")
            return redirect('/mensajes/')
    

    

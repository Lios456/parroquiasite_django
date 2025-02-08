from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import *
from django.core.mail import send_mail
from django.contrib.auth import login, logout, authenticate
from django.core.paginator import Paginator

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth.forms import UserCreationForm

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


def liturgia(request):
    return render(request, 'liturgia.html')

def calendarios(request):
    return render(request, 'calendarios.html')

def horarios(request):
    return render(request, 'horarios.html')
def sacramentos(request):
    return render(request, 'sacramentos.html')

def oracion(request):
    return render(request, 'oracion.html')

def galeria(request):
    return render(request, 'galeria.html')

def news(request):
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

    noticias = Noticia.objects.all().order_by('-fecha')  # Ordenar por la más reciente
    paginator = Paginator(noticias, 5)  # 5 noticias por página

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'noticias': page_obj
    }
    return render(request, 'noticias.html', context)

def new(request,id):
    try:
        noticia = get_object_or_404(Noticia, id=id)
        context = {
            'noticia': noticia
        }
        return render(request, 'noticia.html', context)
    except Exception as e:
        messages.error(request, "No existe ninguna noticia")
        return redirect('/news/')

@login_required(login_url='/login/')
@staff_member_required(login_url='/login/')
def delete_new(request,id):
    if request.method == 'POST':
        try:
            noticia = Noticia.objects.get(id=id)
            noticia.delete()
            messages.success(request, 'Noticia eliminada con éxito')
            return redirect('/news/')
        except:
            messages.error(request, "No existe ninguna noticia")
            return redirect('/news/')

@login_required(login_url='/login/')
@staff_member_required(login_url='/login/')
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

@login_required(login_url='/login/')
@staff_member_required(login_url='/login/')
def mensajes(request):
    mensajes = Mensaje.objects.all().order_by('-id') 
    paginator = Paginator(mensajes, 5) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'mensajes.html', {'page_obj': page_obj})

@login_required(login_url='/login/')
@staff_member_required(login_url='/login/')
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
    


"""
CRUD PARA PERSONAS
"""

class PersonaListView(ListView):
    model = Persona
    template_name = 'persona_list.html'
    context_object_name = 'personas'

class PersonaCreateView(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'persona_form.html'
    success_url = reverse_lazy('persona_list')

class PersonaUpdateView(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'persona_form.html'
    success_url = reverse_lazy('persona_list')

class PersonaDeleteView(DeleteView):
    model = Persona
    template_name = 'persona_confirm_delete.html'
    success_url = reverse_lazy('persona_list')



"""
RESERVA DE MISAS
"""
@login_required(login_url='/login/')
def solicitar_misa(request):
    if request.method == 'POST':
        form = ReservaMisaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.usuario = request.user  # Asignamos el usuario logueado
            reserva.save()
            # 📧 Enviar correo al usuario
            subject_user = "Confirmación de tu solicitud de Misa"
            body_user = f"""
            Hola {request.user.username},

            Hemos recibido tu solicitud y nos pondremos en contacto contigo lo antes posible.

            Detalles de tu mensaje:
            -----------------------
            Fecha: {reserva.fecha}
            Hora: {reserva.hora}
            Intenciones: {reserva.intenciones}

            Gracias por contactarnos.

            Atentamente,
            Santísima Trinidad La Laguna
            """

            send_mail(
                subject_user,
                body_user,
                'santisimatrinidadlalaguna@gmail.com',  # Remitente
                [request.user.email],  # Destinatario: usuario que llenó el formulario
                fail_silently=False,
            )
            messages.success(request, 'Tu solicitud de misa ha sido enviada con éxito, revisa tu correo')
            return redirect('/')
        else:
            messages.error(request, 'Hubo un error al enviar tu solicitud. Inténtalo de nuevo.')
    else:
        form = ReservaMisaForm()

    return render(request, 'solicitar_misa.html', {'form': form})

@login_required(login_url='/login/')
@staff_member_required(login_url='/login/')
def ver_solicitudes(request):
    reservas = ReservaMisa.objects.all()
    return render(request, 'ver_solicitudes.html', {'reservas': reservas})


def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # Usar el formulario personalizado
        if form.is_valid():
            form.save()
            messages.success(request, 'Cuenta creada exitosamente. Puedes iniciar sesión.')
            return redirect('/login/')
        else:
            messages.error(request, 'Hubo un error en el registro. Intenta nuevamente.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registro.html', {'form': form})


"""
RESERVA DE BAUTISMOS
"""
@login_required(login_url='/login/')
def solicitar_bautizo(request):
    if request.method == 'POST':
        form = BautizoForm(request.POST)
        if form.is_valid():
            bautizo = form.save(commit=False)
            bautizo.usuario = request.user  # Asignamos el usuario logueado
            bautizo.save()
            # 📧 Enviar correo al usuario
            subject_user = "Confirmación de tu solicitud de Bautizo"
            body_user = f"""
            Hola {request.user.username},

            Hemos recibido tu solicitud de bautizo y nos pondremos en contacto contigo lo antes posible.

            Detalles de tu solicitud:
            -------------------------
            Fecha: {bautizo.fecha}
            Hora: {bautizo.hora}
            Nombre del Niño/Niños: {bautizo.nombre_nino}
            Nombre del Padre: {bautizo.nombre_padre}
            Nombre de la Madre: {bautizo.nombre_madre}
            Padrinos: {bautizo.padrinos}
            Observaciones: {bautizo.observaciones}

            Gracias por contactarnos.

            Atentamente,
            Santísima Trinidad La Laguna
            """

            send_mail(
                subject_user,
                body_user,
                'santisimatrinidadlalaguna@gmail.com',  # Remitente
                [request.user.email],  # Destinatario: usuario que llenó el formulario
                fail_silently=False,
            )
            messages.success(request, 'Tu solicitud de bautizo ha sido enviada con éxito, revisa tu correo')
            return redirect('/')
        else:
            messages.error(request, 'Hubo un error al enviar tu solicitud. Inténtalo de nuevo.')
    else:
        form = BautizoForm()

    return render(request, 'solicitar_bautizo.html', {'form': form})

@login_required(login_url='/login/')
@staff_member_required(login_url='/login/')
def ver_solicitudes_bautizos(request):
    bautizos = Bautizo.objects.all()
    return render(request, 'ver_solicitudes_bautizos.html', {'bautizos': bautizos})

@login_required(login_url='/login/')
def solicitar_matrimonio(request):
    if request.method == 'POST':
        form = MatrimonioForm(request.POST)
        if form.is_valid():
            matrimonio = form.save(commit=False)
            matrimonio.usuario = request.user  # Asignamos el usuario logueado
            matrimonio.save()
            # 📧 Enviar correo al usuario
            subject_user = "Confirmación de tu solicitud de Matrimonio"
            body_user = f"""
            Hola {request.user.username},

            Hemos recibido tu solicitud de matrimonio y nos pondremos en contacto contigo lo antes posible.

            Detalles de tu solicitud:
            -------------------------
            Fecha: {matrimonio.fecha}
            Hora: {matrimonio.hora}
            Nombre del Novio: {matrimonio.nombre_novio}
            Nombre de la Novia: {matrimonio.nombre_novia}
            Padrinos: {matrimonio.padrinos}
            Observaciones: {matrimonio.observaciones}

            Gracias por contactarnos.

            Atentamente,
            Santísima Trinidad La Laguna
            """

            send_mail(
                subject_user,
                body_user,
                'santisimatrinidadlalaguna@gmail.com',  # Remitente
                [request.user.email],  # Destinatario: usuario que llenó el formulario
                fail_silently=False,
            )
            messages.success(request, 'Tu solicitud de matrimonio ha sido enviada con éxito, revisa tu correo')
            return redirect('/')
        else:
            messages.error(request, 'Hubo un error al enviar tu solicitud. Inténtalo de nuevo.')
    else:
        form = MatrimonioForm()

    return render(request, 'solicitar_matrimonio.html', {'form': form})

@login_required(login_url='/login/')
@staff_member_required(login_url='/login/')
def ver_solicitudes_matrimonios(request):
    matrimonios = Matrimonio.objects.all()
    return render(request, 'ver_solicitudes_matrimonios.html', {'matrimonios': matrimonios})
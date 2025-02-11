from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta

# Create your models here.

class Mensaje(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.TextField()
    message = models.TextField()

    def __str__(self):
        return f'Mensaje de {self.name} | Detalle: {self.message}'


class Noticia(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.titulo}'
    
class Persona(models.Model):
    apellido1 = models.CharField(max_length=100, verbose_name='Apellido Paterno')
    apellido2 = models.CharField(max_length=100, verbose_name='Apellido Materno')
    nombres = models.CharField(max_length=100, verbose_name='Nombres')
    direccion = models.TextField(verbose_name='Dirección')
    celular = models.CharField(max_length=15, verbose_name='Celular')
    email = models.EmailField(verbose_name='Email')

    def __str__(self):
        return f"{self.nombres} {self.apellido1} {self.apellido2}"
    

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'apellido1': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido2': forms.TextInput(attrs={'class': 'form-control'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

"""
RESERVA DE MISAS
"""
from django.utils import timezone

class ReservaMisa(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField()
    intenciones = models.TextField()
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')
    fecha_creacion = models.DateTimeField(default=timezone.now)  # Valor predeterminado explícito
    
    def __str__(self):
        return f"Reserva de misa - {self.usuario.username} - {self.fecha} {self.hora}"
    
class ReservaMisaForm(forms.ModelForm):
    class Meta:
        model = ReservaMisa
        fields = ['fecha', 'intenciones']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'intenciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa tu correo electrónico'
        })
    )

    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Crea una contraseña segura',
            'data-bs-toggle': 'tooltip',
            'data-bs-placement': 'right',
            'title': 'La contraseña debe tener al menos 8 caracteres, una letra mayúscula, una minúscula, un número y un carácter especial.'
        }),
        help_text="La contraseña debe tener al menos 8 caracteres, una letra mayúscula, una minúscula, un número y un carácter especial."
    )

    password2 = forms.CharField(
        label="Confirmar Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirma tu contraseña',
            'data-bs-toggle': 'tooltip',
            'data-bs-placement': 'right',
            'title': 'Repite la contraseña para confirmar.'
        }),
        help_text="Repite la contraseña para confirmar."
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingresa un nombre de usuario'
            }),
        }
"""
BAUTIZOS
"""
class Bautizo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField()
    nombre_nino = models.CharField(max_length=200, verbose_name='Nombre del Niño/Niños')
    nombre_padre = models.CharField(max_length=200, verbose_name='Nombre del Padre')
    nombre_madre = models.CharField(max_length=200, verbose_name='Nombre de la Madre')
    padrinos = models.CharField(max_length=200)
    observaciones = models.TextField(blank=True, null=True)

    def clean(self):
        # Validar que la fecha no sea anterior a la fecha actual y tenga al menos una semana de anticipación
        if self.fecha < timezone.now().date():
            raise ValidationError("La fecha no puede ser anterior a la actual.")
        if self.fecha < (timezone.now() + timedelta(weeks=1)).date():
            raise ValidationError("La fecha debe tener al menos una semana de anticipación.")

    def __str__(self):
        return f"Bautizo - {self.usuario.username} - {self.fecha} {self.hora}"

class BautizoForm(forms.ModelForm):
    class Meta:
        model = Bautizo
        fields = ['fecha', 'nombre_nino', 'nombre_padre', 'nombre_madre', 'padrinos', 'observaciones']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'nombre_nino': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_padre': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_madre': forms.TextInput(attrs={'class': 'form-control'}),
            'padrinos': forms.TextInput(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        
"""
MATRIMONIOS
"""
class Matrimonio(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField()
    nombre_novio = models.CharField(max_length=200, verbose_name='Nombre del Novio')
    nombre_novia = models.CharField(max_length=200, verbose_name='Nombre de la Novia')
    padrinos = models.CharField(max_length=200)
    observaciones = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Matrimonio - {self.usuario.username} - {self.fecha} {self.hora}"
    
class MatrimonioForm(forms.ModelForm):
    class Meta:
        model = Matrimonio
        fields = ['fecha', 'nombre_novio', 'nombre_novia', 'padrinos', 'observaciones']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'nombre_novio': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_novia': forms.TextInput(attrs={'class': 'form-control'}),
            'padrinos': forms.TextInput(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
    
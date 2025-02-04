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
class ReservaMisa(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    intenciones = models.TextField()

    def __str__(self):
        return f"Reserva de misa - {self.usuario.username} - {self.fecha} {self.hora}"
    
class ReservaMisaForm(forms.ModelForm):
    class Meta:
        model = ReservaMisa
        fields = ['fecha', 'hora', 'intenciones']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'intenciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.TextInput(attrs={'class': 'form-control'}),
            'password2': forms.TextInput(attrs={'class': 'form-control'})
        }

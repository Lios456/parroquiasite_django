from django.db import models
from django.contrib.auth.models import User
from django import forms
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


from dataclasses import field
from msilib.schema import CheckBox
from pyexpat import model
from django import forms
from django.forms import ModelForm, fields, Form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#from pkg_resources import require
#from .models import Vehiculo, Producto, Factura, DetalleFactura, ProductosBodega







class RegistrarUsuarioForm(UserCreationForm):


    class Meta:
        model = User
        fields = ['username', 'first_name','last_name', 'email']



class IniciarSesionForm(Form):
    username = forms.CharField(widget=forms.TextInput(), label="Correo")
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
    class Meta:
        fields = ['username', 'password']
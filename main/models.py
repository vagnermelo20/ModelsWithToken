from django.db import models
from main.utils import estados_brasil, TIPO_USER_CHOICES
# Create your models here.

ESTADOS_CHOICES = [(estado, estado) for estado in estados_brasil]

class Usuario(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    telefone = models.CharField(max_length=100, null=True, blank=True)
    documento = models.CharField(max_length=100, null=True, blank=True)
    tipo_user = models.CharField(max_length=100,choices=TIPO_USER_CHOICES,null=True,blank=True)
    
    def __str__(self):
        return self.nome
    
class Endereco(models.Model):
    estado = models.CharField(max_length=100,choices=ESTADOS_CHOICES,null=True,blank=True)
    municipio = models.CharField(max_length=100, null=True, blank=True)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    logradouro = models.CharField(max_length=100, null=True, blank=True)
    numero = models.CharField(max_length=100, null=True, blank=True)
    cep = models.CharField(max_length=100, null=True, blank=True)
    usuario = models.ForeignKey (Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.usuario.nome
    
class Visitante(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    telefone = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.nome
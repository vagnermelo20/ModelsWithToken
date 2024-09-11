from rest_framework import serializers
from .models import Usuario, Endereco , Visitante

class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
    
class EnderecoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'
    
class VisitanteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Visitante
        fields = '__all__'
#teste
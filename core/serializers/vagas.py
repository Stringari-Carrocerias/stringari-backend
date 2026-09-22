from rest_framework.serializers import ModelSerializer
from django.core.exceptions import ValidationError

from core.models import Vaga

class VagaSerializer(ModelSerializer):
    class Meta:
        model = Vaga
        fields = '__all__'
        
    # def validate_salario(self, salario):
    #     if salario == 0:
    #         raise ValidationError('O salário deve ser maior que zero')
    #     return salario 
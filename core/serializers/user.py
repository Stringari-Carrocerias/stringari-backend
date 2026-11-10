import re

from rest_framework.serializers import CharField, ModelSerializer, SlugRelatedField, ValidationError
from validate_docbr import CNPJ

from core.models import User
from uploader.models import Image
from uploader.serializers import ImageSerializer


class UserSerializer(ModelSerializer):
    foto_attachment_key = SlugRelatedField(
        source='foto',
        queryset=Image.objects.all(),
        slug_field='attachment_key',
        required=False,
        write_only=True,
        allow_null=True,
    )
    foto = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'foto',
            'foto_attachment_key',
            'fullName',
            'phone',
            'name',
            'cnpj',
            'address',
            'razao_social',
            'is_active',
            'is_staff',
            'is_superuser',
            'last_login',
            'groups',
        ]

    def validate_fullName(self, value):
        if value is not None and any(char.isdigit() for char in value):
            raise ValidationError('O nome completo não pode conter números.')
        return value


class UserRegistrationSerializer(ModelSerializer):
    password = CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class CustomerCNPJSerializer(ModelSerializer):
    password = CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['id', 'email', 'fullName', 'phone', 'cnpj', 'address', 'razao_social', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def validate_fullName(self, value):
        if not value or not value.strip():
            raise ValidationError('Nome completo inválido. Preencha os campos corretamente.')

        if any(char.isdigit() for char in value):
            raise ValidationError('O nome completo não pode conter números.')
        return value

    def validate_phone(self, phone):
        pattern = r'^\(\d{2}\) \d{5}-\d{4}$'

        if not phone or not phone.strip():
            raise ValidationError('Número de telefone inválido. Preencha os campos corretamente.')

        if not re.fullmatch(pattern, phone):
            raise ValidationError('Telefone inválido. Use o formato (47) 99999-9999.')
        return phone

    def validate_cnpj(self, cnpj):
        validator = CNPJ()

        if not validator.validate(cnpj):
            raise ValidationError('CNPJ inválido. Preencha os campos corretamente.')
        return cnpj

    def validate_address(self, value):
        if not value or not value.strip():
            raise ValidationError('Endereço inválido. Preencha o campo corretamente.')

        return value

    def validate_razao_social(self, value):
        if not value or not value.strip():
            raise ValidationError('Razão social inválida. Preencha os campos corretamente.')
        return value


class CustomerCPFSerializer(ModelSerializer):
    password = CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['id', 'email', 'fullName', 'phone', 'address', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def validate_fullName(self, value):
        if not value or not value.strip():
            raise ValidationError('Nome completo inválido. Preencha os campos corretamente.')

        if any(char.isdigit() for char in value):
            raise ValidationError('O nome completo não pode conter números.')
        return value

    def validate_phone(self, phone):
        pattern = r'^\(\d{2}\) \d{5}-\d{4}$'

        if not phone or not phone.strip():
            raise ValidationError('Número de telefone inválido. Preencha os campos corretamente.')

        if not re.fullmatch(pattern, phone):
            raise ValidationError('Telefone inválido. Use o formato (47) 99999-9999.')
        return phone

    def validate_address(self, value):
        if not value or not value.strip():
            raise ValidationError('Endereço inválido. Preencha o campo corretamente.')

        return value

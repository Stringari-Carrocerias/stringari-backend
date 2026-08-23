from rest_framework import serializers
from rest_framework.serializers import CharField, ModelSerializer, SlugRelatedField, ValidationError

from core.models import User
from uploader.models import Image
from uploader.serializers import ImageSerializer

class UserSerializer(ModelSerializer):

    foto_attachment_key = SlugRelatedField(source='foto', queryset=Image.objects.all(), slug_field='attachment_key', required=False, write_only=True, allow_null=True)
    foto = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'foto', 'foto_attachment_key', 'fullName', 'phone', 'name', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'groups']
        depth = 1

    def validate_fullName(self, value):
        if value != None and any(char.isdigit() for char in value):
            raise ValidationError('O nome completo não pode conter números.')
        return value



class UserRegistrationSerializer(ModelSerializer):
    password = CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

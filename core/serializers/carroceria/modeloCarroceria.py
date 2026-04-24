from rest_framework.serializers import ModelSerializer, SlugRelatedField

from core.models import ModeloCarroceria
from uploader.models import Image
from uploader.serializers import ImageSerializer


class ModeloCarroceriaRetrieveSerializer(ModelSerializer):
    imagem = ImageSerializer(required=True)

    class Meta:
        model = ModeloCarroceria
        fields='__all__'
        depth = 1

class ModeloCarroceriaSerializer(ModelSerializer):
    imagem_attachment_key = SlugRelatedField(
        source='imagem',
        queryset = Image.objects.all(),
        slug_field = 'attachment_key',
        required=False,
        write_only = True,
    )

    imagem = ImageSerializer(required=False, read_only = True)

    class Meta:
        model = ModeloCarroceria
        fields = '__all__';
        depth = 1
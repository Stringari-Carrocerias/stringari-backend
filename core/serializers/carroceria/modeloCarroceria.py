from rest_framework.serializers import ModelSerializer, SlugRelatedField

from core.models import Categoria, ModeloCarroceria
from core.serializers.carroceria.categoria import CategoriaSerializer
from uploader.models import Image
from uploader.serializers import ImageSerializer


class ModeloCarroceriaListSerializer(ModelSerializer):
    class Meta:
        model = ModeloCarroceria
        fields = ['id', 'nome', 'valor', 'comprimento', 'largura', 'altura', 'descricaoCurta', 'imagem', 'categoria']
        depth = 1


class ModeloCarroceriaRetrieveSerializer(ModelSerializer):
    imagem = ImageSerializer(required=True)

    class Meta:
        model = ModeloCarroceria
        fields = '__all__'
        depth = 1


class ModeloCarroceriaCreateUpdateSerializer(ModelSerializer):
    imagem_attachment_key = SlugRelatedField(
        source='imagem', queryset=Image.objects.all(), slug_field='attachment_key', required=False, write_only=True
    )

    imagem = ImageSerializer(required=False, read_only=True)

    categoria_send = SlugRelatedField(
        queryset=Categoria.objects.all(), source='categoria', slug_field='nome', required=False, write_only=True
    )

    categoria = CategoriaSerializer(required=False, read_only=True)

    class Meta:
        model = ModeloCarroceria
        fields = '__all__'

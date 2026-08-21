from rest_framework.serializers import ModelSerializer, ValidationError

from uploader.helpers.files import CONTENT_TYPE_JPG, CONTENT_TYPE_PNG
from uploader.models import Image


class ImageUploadSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ["attachment_key", "file", "description", "uploaded_on", "url"]
        read_only_fields = ["attachment_key", "uploaded_on", "url"]
        extra_kwargs = {"file": {"write_only": True}}

    def validate_file(self, value):
        valid_content_types = [CONTENT_TYPE_JPG, CONTENT_TYPE_PNG]
        if value.content_type not in valid_content_types:
            raise ValidationError("Invalid or corrupted image.")
        return value


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ["url", "description"]
        read_only_fields = ["url", "attachment_key"]

    def create(self, validated_data):
        raise NotImplementedError("Use ImageUploadSerializer to create images.")
from rest_framework.serializers import ModelSerializer
from .models import Notes

class NoteSerializers(ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'
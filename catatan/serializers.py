from rest_framework import serializers
from catatan.models import Note


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'body', 'tags', 'createdAt', 'updatedAt']
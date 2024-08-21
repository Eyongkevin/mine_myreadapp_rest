from rest_framework import serializers
from apps.book.models import Tag

class TagSerializer(serializers.ModelSerializer):
    # TODO: Modify 'name' to return a capitalized tag name
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.name.capitalize()

    class Meta:
        model = Tag 
        fields = '__all__'
        read_only_fields = ('id', )
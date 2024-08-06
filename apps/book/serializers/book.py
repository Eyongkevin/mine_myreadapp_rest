from rest_framework import serializers
from apps.book.models import Book
from . import AuthorSerializer, TagSerializer, BookAuthorSerializer
from apps.core.constants import BOOK_CATEGORY

class CreateBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        # authors has an expicit intermediate table.
        exclude = ('authors', )

class ReadBookSerializer(serializers.ModelSerializer):
    # If you want more control over the relationship
    # tags = TagSerializer(many=True)
    # Do this later
    category = serializers.SerializerMethodField()

    def get_category(self, obj):
        return BOOK_CATEGORY.get(obj.category)
    
    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data['authors'] = BookAuthorSerializer(.authors.all(), many=True).data


    class Meta:
        model = Book
        fields = '__all__'
        depth = 1 # If you don't want control over the relationship

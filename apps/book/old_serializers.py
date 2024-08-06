from rest_framework import serializers
from .models import Author

# To seralizer the Author model, ensure that
# - The name should be same as that of the model, or you use `source`
# in case you want to rename the attribute

# - The data type here is exactly what is in the model
# - Or a data type casting is possible between the types.

class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def create(self, validated_data):
        return Author.objects.get_or_create(**validated_data)

class TagSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

class BookSerializer(serializers.Serializer):
    isbn = serializers.CharField()
    title = serializers.CharField()
    # no TextField
    # someone once said, a TextField is just a CharField with no max_length
    # was it you Terence?
    description = serializers.CharField() 
    page_count = serializers.IntegerField()
    category = serializers.CharField()
    published_date = serializers.IntegerField()
    publisher = serializers.CharField()
    authors = AuthorSerializer(many=True)
    lang = serializers.CharField()
    edition = serializers.IntegerField()
    book_format= serializers.CharField()
    tags = TagSerializer(many=True)



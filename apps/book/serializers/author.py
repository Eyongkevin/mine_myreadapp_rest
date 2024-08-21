from rest_framework import serializers
from apps.book.models import Author, BookAuthor


class AuthorSerializer(serializers.ModelSerializer):
    # names = serializers.CharField()
    names = serializers.SerializerMethodField() # read_only by default

    # def get_names(self, obj): # get_<field-name>
    #     return f'{obj.first_name} {obj.last_name}'


    def validate_first_name(self, value): # validate_<field-name>
        """Field level validation of first_name"""

        if '-' in value:
            raise serializers.ValidationError('first_name should not have the character -')
        return value
    
    def validate(self, attrs):
        """Object level validation"""

        if attrs.get('first_name') == attrs.get('last_name'):
            raise serializers.ValidationError('first_name and last_name cannot have same value')
        return attrs

    class Meta:
        model = Author 
        fields = '__all__'
        read_only_fields = ('id', )


class BookAuthorSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = BookAuthor
        fields = ('author', 'role')
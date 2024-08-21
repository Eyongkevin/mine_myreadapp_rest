from rest_framework import serializers
from django.contrib.auth.models import User
from .nic import NicSerializer
from apps.reader.models import Reader

class ReadUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User 
        exclude = ('password',)

class ReadReaderSerializer(serializers.ModelSerializer):
    # Without this, even the password will be exposed.
    user = ReadUserSerializer()
    # nic = NicSerializer()
    class Meta:
        model = Reader
        fields = '__all__'
        read_only_fields = ('id', )
        depth = 1 # comment out 'nic' above then remove `depth` to have more control

class CreateReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader 
        fields ='__all__'
        read_only_fields = ('id', )
from rest_framework import serializers
from apps.reader.models import NIC


class NicSerializer(serializers.ModelSerializer):

    class Meta:
        model = NIC
        fields = '__all__'
        read_only_fields = ('id', 'expiration_date')
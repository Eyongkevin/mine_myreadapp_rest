from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.book import models 
from apps.book import serializers

@api_view(['GET'])
def list_tags(request):
    tags = models.Tag.objects.all()

    data = serializers.TagSerializer(tags, many=True)
    
    return Response({'data': data.data}, status=status.HTTP_200_OK)

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from apps.book import models
from apps.book import serializers

# Create your views here.

@api_view(['GET'])
def list_authors(request):
    # Get data
    authors = models.Author.objects.all()

    # Serialize
    data = serializers.AuthorSerializer(authors, many=True)

    # Return 
    return Response({'data': data.data}, status=status.HTTP_200_OK)


class DetailAuthor(generics.RetrieveAPIView):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer

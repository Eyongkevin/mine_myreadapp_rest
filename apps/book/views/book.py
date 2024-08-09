from django.db import transaction
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from apps.book import serializers
from apps.book import models


@api_view(['GET'])
def list_books(request, pk=None):
    if pk:
        books = models.Book.objects.filter(pk=pk)
    else:
        books = models.Book.objects.all()

    data = serializers.ReadBookSerializer(books, many=True)

    return Response({'data': data.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_book(request):
    with transaction.atomic():
        data = request.data

        # even if I don't pop it, the serializer will clean it out
        authors = data.pop('authors')

        book = serializers.CreateBookSerializer(data=data)

        if book.is_valid():
            book = book.save()
        
        for author in authors:
            book.authors.add(
                models.Author.objects.get(pk=author['id']),
                through_defaults={'role': author['role']})
    return Response({'detail': 'Book Created Successfully'}, status=status.HTTP_201_CREATED)
        



class BooksView(APIView):
    permission_classes = (IsAdminUser, )

    # GET
    def get(self, request):
        books = models.Book.objects.all()
        data = serializers.ReadBookSerializer(books, many=True)

        return Response({'data': data.data}, status=status.HTTP_200_OK)

    # POST 
    def post(self, request):
        pass 

    # DELETE
    def delete(self, request):
        pass

    # UPDATE
    def put(self, request):
        pass
    def patch(self, request):
        pass


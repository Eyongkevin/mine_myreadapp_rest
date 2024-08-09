from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from .permissions import IsOwnReader
from .serializers import ReaderSerializer

from .models import Reader

class Login(APIView):
    def post(self, request):
        password = request.data.get("password")
        username = request.data.get("username")

        user = authenticate(
            username=username,
            password=password,
        )
        if not user:
            return Response(
                {"error": "Password or Username incorrect"},
                status=status.HTTP_404_NOT_FOUND,
            )
        token, _ = Token.objects.get_or_create(user=user)
        # I am not returning the user, together with the token.
        return Response(
            {"token": token.key},
            status=status.HTTP_201_CREATED,
        )

# viewsets.ReadOnlyModelViewSet only allows list and retrieve.
class ReaderViewSet(viewsets.ModelViewSet):
    permission_classes = (IsOwnReader, )
    queryset = (
        Reader.objects.select_related("user", "nic")
        .all()
    )
    serializer_class = ReaderSerializer

    def list(self, request, *args, **kwargs):
        return Response({'error': 'NotImplemented'}, status=status.HTTP_406_NOT_ACCEPTABLE)
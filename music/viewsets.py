from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Perfil
from .serializer import PerfilSerializer

class PerfilViewSet(APIView):
    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.id = None

    def get(self, id):
        self.id = id
        if id:
            perfil = get_object_or_404(Perfil, id=id)
            serializer = PerfilSerializer(perfil)
            return Response(serializer.data, status=status.HTTP_200_OK)
        perfis = Perfil.objects.all()
        serializer = PerfilSerializer(perfis, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request):
        serializer = PerfilSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def put(request, id):
        perfil = get_object_or_404(Perfil, id=id)
        serializer = PerfilSerializer(perfil, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(id):
        perfil = get_object_or_404(Perfil, id=id)
        perfil.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

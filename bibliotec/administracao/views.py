from django.shortcuts import render, render_to_response
from .models import Livro, Cliente, Reserva
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .serializers import LivroSerializer, ClienteSerializer, ReservaSerializer


# Create your views here.
#
# def listar_livros(request):
#     livros = Livro.objects.all()
#     return render_to_response("livros.html", {"livros":livros})


class Livros(APIView):

    def get(self, request):

        livros = Livro.objects.all()
        id_livro = self.request.query_params.get('pk', None)

        if id_livro:
            livros = Livro.objects.filter(id_livro=id_livro)

        serializer = LivroSerializer(livros, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = LivroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LivroDetails(APIView):


    def get(self, request, pk):
        livros = Livro.objects.filter(id_livro=pk)
        serializer = LivroSerializer(livros, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, pk, format=None):
        livro = Livro.objects.get(pk=pk)
        serializer = LivroSerializer(livro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request,pk):
        livro = Livro.objects.filter(id_livro=pk)
        if livro:
            livro.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"result": "O id informado não existe!"}, status=status.HTTP_404_NOT_FOUND)


class Clientes(APIView):

    def get(self, request):

        clientes = Cliente.objects.all()
        id_cliente = self.request.query_params.get('pk', None)

        if id_cliente:
            clientes = Cliente.objects.filter(id_cliente=id_cliente)

        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClienteDetails(APIView):


    def get(self, request, pk):
        cliente = Cliente.objects.filter(id_cliente=pk)
        serializer = ClienteSerializer(cliente, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, pk, format=None):
        cliente = Cliente.objects.get(pk=pk)
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request,pk):
        cliente = Cliente.objects.filter(id_cliente=pk)
        if cliente:
            cliente.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"result": "O id informado não existe!"}, status=status.HTTP_404_NOT_FOUND)



class Reservas(APIView):

    def get(self, request, pk):

        reservas = Reserva.objects.filter(cliente=pk)

        serializer = ReservaSerializer(reservas, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ReservaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
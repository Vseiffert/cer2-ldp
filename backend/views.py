from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from backend.models import Number, Pokemon
from backend.serializers.NumberSerializer import NumberSerializer
from backend.serializers.PokemonSerializer import PokemonSerializer


import random
import string

class NumberViewSet(viewsets.ModelViewSet):

    queryset = Number.objects.all()
    serializer_class = NumberSerializer

    def get_queryset(self):
        """
        Opcionalmente restringe los números devueltos al valor de 'number' que
        sea igual a 10, pasando un parámetro de consulta `number=10` en la URL.
        """
        queryset = Number.objects.all()
        number = self.request.query_params.get('number', None)
        if number is not None:
            queryset = queryset.filter(number=number)
        return queryset

class PokemonListAPIView(APIView):
    def get(self, request):
        pokemons = Pokemon.objects.all()
        serializer = PokemonSerializer(pokemons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    
    def list(self, request):
        pokemons = self.get_queryset() #se obtienen los datos
        return render(request, 'pokemon_list.html', {'pokemons': pokemons}) #se renderiza la imagen

    # def get_queryset(self):
    #     """
    #     Opcionalmente restringe los números devueltos al valor de 'number' que
    #     sea igual a 10, pasando un parámetro de consulta `number=10` en la URL.
    #     """
    #     queryset = Number.objects.all()
    #     number = self.request.query_params.get('number', None)
    #     if number is not None:
    #         queryset = queryset.filter(number=number)
    #     return queryset

class CreateRandomNumber(generics.CreateAPIView):
    serializer_class = NumberSerializer

    def perform_create(self, serializer):
        # Generar un número aleatorio entre 1 y 100
        random_number = random.randint(1, 100)
        # Generar una letra aleatoria
        random_letter = random.choice(string.ascii_uppercase)
        # Guardar el número y la letra aleatorios en la base de datos
        serializer.save(number=random_number, letter=random_letter)
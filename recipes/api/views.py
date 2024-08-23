from rest_framework import generics
from .models import Recipe
from .serializers import RecipeSerializer

class RecipeCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

from rest_framework import generics
from .models import Recipe
from .serializers import RecipeSerializer

class RecipeListView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeDetailView(generics.RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

# Create your views here.
from .serializers import AuthorSerializer, BookSerializer, BiographySerializer, ArticleSerializer
from .models import Author, Book, Biography, Article

class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographySerializer

class ArticleModelViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
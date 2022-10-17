from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from .filters import ArticleFilter
from rest_framework.pagination import LimitOffsetPagination

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
"""
class ArticleQuerysetFilterViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Article.objects.all()

    def get_queryset(self):
        return Article.objects.filter(name__contains='python')

class ArticleKwargsFilterView(ListAPIView):
    serializer_class = ArticleSerializer
    def get_queryset(self):
        name = self.kwargs['name']
        return Article.objects.filter(name__contains=name)

class ArticleParamFilterViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    def get_queryset(self):
        name = self.request.query_params.get('name', '')
        articles = Article.objects.all()
        if name:
            articles = articles.filter(name__contains=name)
            return articles
            """
class ArticleCustomDjangoFilterViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_class = ArticleFilter

class ArticleLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
class ArticleLimitOffsetPaginatonViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = ArticleLimitOffsetPagination
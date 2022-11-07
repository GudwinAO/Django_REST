from dataclasses import fields
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Author, Book, Biography, Article


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BiographySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Biography
        fields = '__all__'


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class BookSerializer(serializers.HyperlinkedModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Book
        fields = '__all__'


class BookSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

class UserSerializerWithFullName(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class AuthorSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name',)

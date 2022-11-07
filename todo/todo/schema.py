import graphene
from graphene_django import DjangoObjectType
from authors.models import Book, Author


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = '__all__'


class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    all_authors = graphene.List(AuthorType)

    def resolve_all_books(root, info):
        return Book.objects.all()

    def resolve_all_authors(root, info):
        return Author.objects.all()







schema = graphene.Schema(query=Query)


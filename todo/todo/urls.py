from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from authors.views import AuthorModelViewSet, BookModelViewSet, BiographyModelViewSet, ArticleModelViewSet
from graphene_django.views import GraphQLView

#from .views import UserListAPIView



router = routers.DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('books', BookModelViewSet)
router.register('biography', BiographyModelViewSet)
router.register('article', ArticleModelViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Library",
        default_version='0.1',
        description="Documentation to out project",
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),

    
    #path(r'^api/(?P<version>\d\.\d)/users/$', UserListAPIView.as_view()),
    #path('', UserListAPIView.as_view()),
    #path('api/users/0.1', include('todo.urls', namespace='0.1')),
    #path('api/users/0.2', include('todo.urls', namespace='0.2')),

    path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), 
    name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
    name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
    name='schema-redoc'),


    path("graphql/", GraphQLView.as_view(graphiql=True)),
]


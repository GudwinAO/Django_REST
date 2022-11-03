from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views
#from .views import UserListAPIView

from authors.views import AuthorModelViewSet, BookModelViewSet, BiographyModelViewSet, ArticleModelViewSet


router = routers.DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('books', BookModelViewSet)
router.register('biography', BiographyModelViewSet)
router.register('article', ArticleModelViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    #Lesson_6_token
    path('api-token-auth/', views.obtain_auth_token),
    #re_path(r'^api/(?P<version>\d\.\d)/users/$', UserListAPIView.as_view()),
    #path('', UserListAPIView.as_view()),
    #path('api/users/0.1', include('todo.urls', namespace='0.1')),
    #path('api/users/0.2', include('todo.urls', namespace='0.2')),
]
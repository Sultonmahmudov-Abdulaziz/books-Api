from django.urls import path
from .views import BooksApiView


app_name = 'api'

urlpatterns = [
    path('api/', BooksApiView.as_view(), name='api'),
]
from django.urls import path
from .views import BooksApiView, BooksDetailApiView, ReviewsApiView

app_name = 'api'

urlpatterns = [
    path('places-list/', BooksApiView.as_view(), name="places"),
    path('place-detail/<int:id>/', BooksDetailApiView.as_view(), name="place_detail"),
    path('reviews/', ReviewsApiView.as_view(), name="reviews"),

]
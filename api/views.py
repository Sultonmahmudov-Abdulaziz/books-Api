from django.shortcuts import render
from books.models import Books, Comment
from django.views import View
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import BooksSerializer

class PlaceApiView(APIView):
    def get(self, request):
        books = Books.objects.all()
        serializer = BooksSerializer(books, many=True)
        return Response(data=serializer.data)



class BooksDetailApiView(View):
    def get(self, request, id):
        book = Books.objects.get(id=id)

        data = {
            "id":book.id,
            "description":book.description,
            "image":book.image.url,
            "autor":book.authors
        }

        return JsonResponse(data)

class ReviewsApiView(View):
    def get(self, request):
        comments = Comment.objects.all().select_related('user').select_related('book')

        result = []

        for comment in comments:
            data = {
                "comment_text":comment.comment_text,
                "stars_given":comment.stars_given,
                "created_at":comment.created_at,
                "user":{
                    "user_id":comment.user.id,
                    "username":comment.user.username,
                    "user_image":comment.user.image.url,
                },
                "book":{
                    "book_id":comment.book.id,
                    "book_image":comment.book.image.url
                },
            }

            result.append(data)

        return JsonResponse({"result":result})

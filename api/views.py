
from django.views import View
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BooksSerializer


class BooksApiView(APIView):
    def get(self,request):
        books = Books.objects.all()
        serializer = BooksSerializer(data=books, many=True)
        return JsonResponse(data=serializer.data)
    
# class BooksDetailApiView(View):
#     def get(self,request,pk):
#         book = Books.objects.get(id=pk)


#         data = {
#             'id':book.id,
#             'description' : book.description,
#             'image' : book.image.url,
#         }

#         return JsonResponse(data)
    


# class CommentApiView(View):
#     def get(self,request):

#         comments = Comment.objects.all()

#         rezult = []
#         for comment in comments:
#             data = {
#                 'id':comment.id,
#                 'comment_text' : comment.comment_text,
#                'stars_given' : comment.stars_given,
#                 'user' : comment.user.username,
#                 'book' : comment.book.description,
#             }
#             rezult.append(data) 




       




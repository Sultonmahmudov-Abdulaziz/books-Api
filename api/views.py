from books.models import Book,Comment
from django.views import View
from django.http import JsonResponse


class BooksApiView(View):
    def get(self,request):
        books = Book.objects.all()

        rezult = []

        for book in books: 
            data = {
                'id':book.id,
                'description' : book.description,
                'image' : book.image.url,
            }
           
            rezult.append(data)


        return JsonResponse({"rezult":rezult})
    
class BooksDetailApiView(View):
    def get(self,request,pk):
        book = Book.objects.get(id=pk)


        data = {
            'id':book.id,
            'description' : book.description,
            'image' : book.image.url,
        }

        return JsonResponse(data)
    


class CommentApiView(View):
    def get(self,request):

        comments = Comment.objects.all()

        rezult = []
        for comment in comments:
            data = {
                'id':comment.id,
                'comment_text' : comment.comment_text,
               'stars_given' : comment.stars_given,
                'user' : comment.user.username,
                'book' : comment.book.description,
            }
            rezult.append(data) 




       




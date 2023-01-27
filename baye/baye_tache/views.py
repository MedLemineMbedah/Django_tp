from django.shortcuts import render
from .models import Book
from .models import Reviews

def book_list(request):
    book = Book.objects.latest('id')
    book_list = []
    book_reviews = book.reviews.all()
    book_list.append({'book': book, 'reviews': book_reviews})
    return render(request, 'index.html', {'book_list': book_list})


# Create your views here.

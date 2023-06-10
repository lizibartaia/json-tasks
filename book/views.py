from django.shortcuts import render
from .models import Book

# Create your views here.

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'book/detail.html', {'book': book})

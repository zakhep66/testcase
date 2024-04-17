from django.shortcuts import render
from .models import Book


def book_list(request):
    author = request.GET.get("author")
    genre = request.GET.get("genre")

    books = Book.objects.all()

    if author:
        books = books.filter(author__name=author)

    if genre:
        books = books.filter(genre__name=genre)

    return render(request, "book_list.html", {"books": books})


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, "book_detail.html", {"book": book, "title": book.title})

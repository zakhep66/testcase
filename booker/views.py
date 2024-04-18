import functools

from django.shortcuts import render
from django.db.models import Q

from .models import Book, Genre


def book_list(request):
    selected_genres = request.GET.getlist("selected_genres")

    if selected_genres:
        genre_queries = [Q(genre__name=genre) for genre in selected_genres]

        books = Book.objects.filter(
            functools.reduce(lambda x, y: x | y, genre_queries)
        ).distinct()

    else:
        books = Book.objects.all()

    genres = Genre.objects.all()
    return render(request, "book_list.html", {"books": books, "genres": genres})


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, "book_detail.html", {"book": book, "title": book.title})

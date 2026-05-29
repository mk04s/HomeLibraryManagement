from django.shortcuts import render, get_object_or_404
from manage_books.models import Book, Genre, Author, Publisher, Series, Note

def index(request):
    books = Book.objects.all()
    genres = Genre.objects.all()
    authors = Author.objects.all()
    context = {'books': books, 'genres': genres, 'authors': authors}
    return render(request, 'manage_books/index.html.jinja', context)


def book(request, book_id):
    single_book = get_object_or_404(Book, pk=book_id)
    return render(request, 'manage_books/book.html.jinja', {'book': single_book})


def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'manage_books/authors.html.jinja', {'authors': authors})


def publishers_list(request):
    publishers = Publisher.objects.all()
    return render(request, 'manage_books/publishers.html.jinja', {'publishers': publishers})

def series_list(request):
    series_queryset = Series.objects.all()
    return render(request, 'manage_books/series.html.jinja', {'series_list': series_queryset})


def notes_list(request):
    notes = Note.objects.all()
    return render(request, 'manage_books/note.html.jinja', {'notes': notes})

def genres_list(request):
    genres = Genre.objects.all()
    return render(request, 'manage_books/genres.html.jinja', {'genres': genres})
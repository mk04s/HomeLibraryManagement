from django.shortcuts import render, get_object_or_404

from manage_books.models import Book, Genre, Author, Publisher, Series, Note

def index(request):
    books = Book.objects.all()
    genres = Genre.objects.all()
    authors = Author.objects.all()
    
    
    context = {
        'books': books,
        'genres': genres, 
        'authors': authors
    }
    return render(request, 'manage_books/index.html.jinja', context)

def book(request, book_id):
    
    single_book = get_object_or_404(Book, pk=book_id)
    return render(request, 'manage_books/book.html.jinja', {'book': single_book})

def author(request, author_id):
    single_author = get_object_or_404(Author, pk=author_id)
    return render(request, 'manage_books/author.html.jinja', {'author': single_author})

def publisher(request, publisher_id):
    single_publisher = get_object_or_404(Publisher, pk=publisher_id)
    return render(request, 'manage_books/publisher.html.jinja', {'publisher': single_publisher})

def series(request, series_id):
    single_series = get_object_or_404(Series, pk=series_id)
    return render(request, 'manage_books/series.html.jinja', {'series': single_series})

def note(request, note_id):
    single_note = get_object_or_404(Note, pk=note_id)
    return render(request, 'manage_books/note.html.jinja', {'note': single_note})
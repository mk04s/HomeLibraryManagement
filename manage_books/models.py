from django.db import models
import pytz

# Create your models here.
class Book(models.Model):
    COVERS = [
        ('hardcover', 'Hardcover'),
        ('paperback', 'Paperback'),
        ('ebook', 'E-book'),
        ('audiobook', 'Audiobook'),
    ]

    LANGUAGES = [
        ('english', 'English'),
        ('polish', 'Polish'),
        ('spanish', 'Spanish'),
        ('french', 'French'),
        ('german', 'German'),
        ('chinese', 'Chinese'),
        ('japanese', 'Japanese'),
    ]

    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20, unique=True)
    publication_date = models.DateField()
    pages = models.IntegerField()
    cover = models.CharField(max_length=20, choices=COVERS)
    language = models.CharField(max_length=20, choices=LANGUAGES)
    is_read = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
    authors = models.ManyToManyField('Author', related_name='books')
    publisher = models.ForeignKey('Publisher', on_delete=models.RESTRICT)
    series = models.ForeignKey('Series', on_delete=models.RESTRICT, blank=True, null=True)
    genres = models.ManyToManyField('Genre', related_name='books', blank=True)
    topics = models.ManyToManyField('Topic', related_name='books', blank=True)

class Author(models.Model):
    TITLE = [
        ('ks', 'Ks.'),
        ('bp', 'Bp.'),
        ('dr', 'Dr.'),
        ('prof', 'Prof.'),
    ]

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    alias = models.CharField(max_length=100, blank=True)
    nationality = models.CharField(max_length=100)
    title = models.CharField(max_length=100, choices=TITLE, blank=True, null=True)
class Publisher(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=2, choices=pytz.country_names.items())
    founded_year = models.IntegerField()
    website = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    
class Genre(models.Model): #gatunek książki
    name = models.CharField(max_length=100)


class Series(models.Model): #seria książek
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    authors = models.ManyToManyField(Author, related_name='series_authors', blank=True)
class Topic(models.Model): #tematyka książki
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

class Note(models.Model): #notatka do książki
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
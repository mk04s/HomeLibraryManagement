from django.db import models
import pytz

class Book(models.Model):
    COVERS = [
        ('hardcover', 'Hardcover'),
        ('paperback', 'Paperback'),
        ('ebook', 'E-book'),
        ('audiobook', 'Audiobook'),
    ]

    LANGUAGES = [
        ('english', 'English'),
        ("polish", 'Polish'),
        ('spanish', 'Spanish'),
        ('french', 'French'),
        ('german', 'German'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20, unique=True)
    publication_date = models.DateField()
    pages = models.IntegerField()
    cover = models.CharField(max_length=20, choices=COVERS)
    language = models.CharField(max_length=20, choices=LANGUAGES)
    is_read = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
    authors = models.ManyToManyField('Author', related_name='books', blank=True)
    publisher = models.ForeignKey('Publisher', on_delete=models.RESTRICT)
    series = models.ForeignKey('Series', on_delete=models.RESTRICT, blank=True, null=True)
    genres = models.ManyToManyField('Genre', related_name='books', blank=True)
    topics = models.ManyToManyField('Topic', related_name='books', blank=True)

    def __str__(self):
        return self.title

class Author(models.Model):
    TITLES = [
        ('ks', "Ks."),
        ('dr', "Dr."),
        ('prof', "Prof."),
        ('mr', "Mr."),
        ('ms', "Ms."),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    title = models.CharField(max_length=20, choices=TITLES, blank=True, null=True)
    alias = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        if self.alias:
            return f"{self.first_name} {self.last_name} ({self.alias})"
        return f"{self.first_name} {self.last_name}"

class Publisher(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=2, choices=pytz.country_names.items())
    founded_year = models.IntegerField()
    website = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Series(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Note(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"Notatka do: {self.book.title} ({self.created_at.strftime('%Y-%m-%d')})"
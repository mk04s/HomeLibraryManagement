from django.urls import path
from . import views

app_name = 'manage_books'

urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:book_id>/', views.book, name='book'),
    path('authors/', views.authors_list, name='authors_list'),
    path('publishers/', views.publishers_list, name='publishers_list'),
    path('series/', views.series_list, name='series_list'),
    path('notes/', views.notes_list, name='notes_list'),
    path('genres/', views.genres_list, name='genres_list'),
]

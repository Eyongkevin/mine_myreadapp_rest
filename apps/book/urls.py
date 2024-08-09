from django.urls import path 
from . import views

app_name = 'author-urls'
urlpatterns = [
    path('author/', views.list_authors, name='author-list'),
    path('tag/', views.list_tags, name='tag-list'),
    path('', views.list_books, name='book-list'),
    path('post/', views.create_book, name='book-create'),
    path('book/', views.BooksView.as_view(), name='book-list-cls'),
    path('<str:pk>/', views.list_books, name='book-list'),
    path('author/<int:pk>/', views.DetailAuthor.as_view(), name='author-detail')
    
]

from django.urls import path
from .views import BookListView, BookDetailView, BorrowListView, \
    borrow_book, return_book

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(),
         name='book-detail'),
    path('my-books/', BorrowListView.as_view(), name='my-books-api'),
    path('borrow/<int:book_id>/', borrow_book, name='borrow-book'),
    path('return/<int:borrow_id>/', return_book, name='return-book'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog, name='home'),
    path('signup/reader/', views.reader_signup, name='reader_signup'),
    path('signup/librarian/', views.librarian_signup, name='librarian_signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('catalog/', views.catalog, name='catalog'),
    path('my-books/', views.my_books, name='my_books'),
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('return/<int:borrow_id>/', views.return_book, name='return_book'),
    path('debtors-list/', views.debtors_list, name='debtors_list'),
]

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .forms import ReaderSignUpForm, LibrarianSignUpForm
from .models import Book, Borrow
from .serializers import BookSerializer, BorrowSerializer


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('catalog')
        else:
            return render(request, 'library/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'library/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def reader_signup(request):
    if request.method == 'POST':
        form = ReaderSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('catalog')
    else:
        form = ReaderSignUpForm()
    return render(request, 'library/signup.html', {'form': form})


def librarian_signup(request):
    if request.method == 'POST':
        form = LibrarianSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('debtors_list')
    else:
        form = LibrarianSignUpForm()
    return render(request, 'library/signup.html', {'form': form})


@login_required
def catalog(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'library/catalog.html', {'books': books})


@login_required
def my_books(request):
    borrows = Borrow.objects.filter(reader=request.user, returned_date__isnull=True).order_by('book__title')
    return render(request, 'library/my_books.html', {'borrows': borrows, 'today': timezone.now()})


@api_view(['POST'])
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if book.available:
        book.available = False
        book.save()
        Borrow.objects.create(book=book, reader=request.user)
        return Response({'status': 'Book borrowed'})
    return Response({'status': 'Book not available'}, status=400)


@api_view(['POST'])
def return_book(request, borrow_id):
    borrow = get_object_or_404(Borrow, id=borrow_id)
    if borrow.reader == request.user and not borrow.returned_date:
        borrow.returned_date = timezone.now()
        borrow.save()
        borrow.book.available = True
        borrow.book.save()
        return Response({'status': 'Book returned'})
    return Response({'status': 'Invalid operation'}, status=400)


@login_required
def debtors_list(request):
    if not request.user.is_superuser and not hasattr(request.user, 'librarian'):
        return redirect('catalog')
    borrows = Borrow.objects.filter(returned_date__isnull=True).order_by('reader__username')
    return render(request, 'library/debtors_list.html', {'borrows': borrows})


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BorrowListView(generics.ListAPIView):
    serializer_class = BorrowSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Borrow.objects.filter(reader=self.request.user, returned_date__isnull=True)

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils import timezone

class Librarian(AbstractUser):
    employee_number = models.CharField(max_length=20)
    groups = models.ManyToManyField(Group, related_name='librarian_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='librarian_permissions')

    def __str__(self):
        return self.username

class Reader(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.TextField()
    groups = models.ManyToManyField(Group, related_name='reader_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='reader_permissions')

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    borrowed_date = models.DateField(auto_now_add=True)
    returned_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.book.title} borrowed by {self.reader.username}'

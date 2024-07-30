from django.contrib import admin
from .models import Librarian, Reader, Book, Borrow

admin.site.register(Librarian)
admin.site.register(Reader)
admin.site.register(Book)
admin.site.register(Borrow)

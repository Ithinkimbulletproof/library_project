from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Reader, Librarian

class ReaderSignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        help_text='First name'
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        help_text='Last name'
    )
    address = forms.CharField(
        widget=forms.Textarea,
        required=True,
        help_text='Address'
    )

    class Meta:
        model = Reader
        fields = ('username', 'first_name', 'last_name', 'address', 'password1', 'password2')

class LibrarianSignUpForm(UserCreationForm):
    employee_number = forms.CharField(
        max_length=20,
        required=True,
        help_text='Employee number'
    )

    class Meta:
        model = Librarian
        fields = ('username', 'employee_number', 'password1', 'password2')

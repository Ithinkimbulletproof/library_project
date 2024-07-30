from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Reader, Librarian

class ReaderSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Имя')
    last_name = forms.CharField(max_length=30, required=True, help_text='Фамилия')
    address = forms.CharField(widget=forms.Textarea, required=True, help_text='Адрес')

    class Meta:
        model = Reader
        fields = ('username', 'first_name', 'last_name', 'address', 'password1', 'password2')
        labels = {
            'username': 'Имя пользователя',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'address': 'Адрес',
            'password1': 'Пароль',
            'password2': 'Подтверждение пароля',
        }
        help_texts = {
            'username': 'Обязательное поле. Не более 150 символов. Разрешены буквы, цифры и @/./+/-/_ только.',
            'password1': 'Ваш пароль не может быть слишком похож на другую личную информацию. Пароль должен содержать не менее 8 символов. Пароль не может быть общепринятым паролем. Пароль не может состоять только из цифр.',
            'password2': 'Введите тот же пароль, что и раньше, для подтверждения.',
        }

class LibrarianSignUpForm(UserCreationForm):
    employee_number = forms.CharField(max_length=20, required=True, help_text='Номер сотрудника')

    class Meta:
        model = Librarian
        fields = ('username', 'employee_number', 'password1', 'password2')
        labels = {
            'username': 'Имя пользователя',
            'employee_number': 'Номер сотрудника',
            'password1': 'Пароль',
            'password2': 'Подтверждение пароля',
        }
        help_texts = {
            'username': 'Обязательное поле. Не более 150 символов. Разрешены буквы, цифры и @/./+/-/_ только.',
            'employee_number': 'Номер сотрудника',
            'password1': 'Ваш пароль не может быть слишком похож на другую личную информацию. Пароль должен содержать не менее 8 символов. Пароль не может быть общепринятым паролем. Пароль не может состоять только из цифр.',
            'password2': 'Введите тот же пароль, что и раньше, для подтверждения.',
        }

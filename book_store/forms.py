from django import forms
from .models import Book,User

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ["borrower"]


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

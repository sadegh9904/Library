from django import forms
from .models import Book,CustomUser,Borrow
from django.contrib.auth.forms import UserCreationForm

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = "__all__"


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = CustomUser
        fields = ["username","email", "password1", "password2"]



class BorrowForm(forms.ModelForm):  
    class Meta:
        model = Borrow
        fields = []

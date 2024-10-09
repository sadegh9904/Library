from django import forms
from .models import Book,Borrower

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ["borrower"]


class BorrowerForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = "__all__"

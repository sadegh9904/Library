from django import forms
from .models import Book,User,Borrow

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = "__all__"


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"



class   BorrowForm(forms.ModelForm):  
    class Meta:
        model = Borrow
        fields = ("book")

    def clean_book(self):
        book = self.cleaned_data["book"]

        if book and not book.is_available:
            raise forms.ValidationError("This book is unavailable right now!")
        
        return book
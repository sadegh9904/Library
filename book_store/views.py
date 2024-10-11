from django.shortcuts import render,redirect
from django.views import View
from django.utils import timezone
from django.views.generic import ListView,UpdateView,DeleteView
from django.views.generic.edit import CreateView,
from .models import User,Book,Borrow
from .forms import BookForm,UserForm
# Create your views here.


class BookListView(ListView):
    model = Book
    template_name = "book_store/book-list.html"
    context_object_name = "books"


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = "book_store/book-create.html"
    success_url = "/book-list"


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = "book_store/book-create.html"
    success_url = "/book-list"


class BookDeleteView(DeleteView):
    model = Book
    template_name = "book_store/book-delete.html"
    success_url = "/book-list"





class UserprofileView(ListView):
    model = User
    template_name = ".html"



class BorrowBookView(CreateView):
    model = User
    form_class = UserForm
    template_name = "book_store/book-borrow.html"
    success_url = "/book-list"

    def form_valid(self, form):
        book = form.cleaned_data["book"]
        user = self.request.user

        borrow = Borrow(
        user=user, book=book, borrow_date = timezone.now(),
        return_date = timezone.now() + timezone.timedelta(days=10)
        )
        
        borrow.save()

        book.is_available = False
        book.save()



        return super().form_valid(form)
    
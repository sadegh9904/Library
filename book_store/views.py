from django.shortcuts import render
from django.views import views
from django.views.generic import ListView,UpdateView,DeleteView
from django.views.generic.edit import CreateView
from .models import User,Book
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





class BorrowerListView(ListView):
    model = User
    template_name = ".html"



class BorrowerCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = ".html"
    success_url = 
    pass

class BorrowerUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = ".html"
    success_url = 
    pass


class BorrowerDeleteView(DeleteView):
    model = User
    form_class = UserForm
    template_name = ".html"
    success_url = 
    pass
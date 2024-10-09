from django.shortcuts import render
from django.views import views
from django.views.generic import ListView,UpdateView,DeleteView
from django.views.generic.edit import CreateView
from .models import Borrower,Book
from .forms import BookForm,BorrowerForm
# Create your views here.


class BookListView(ListView):
    model = Book
    template_name = ".html"



class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = ".html"
    success_url = 


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = ".html"
    success_url = 


class BookDeleteView(DeleteView):
    model = Book
    form_class = BookForm
    template_name = ".html"
    success_url = 





class BorrowerListView(ListView):
    model = Borrower
    template_name = ".html"



class BorrowerCreateView(CreateView):
    model = Borrower
    form_class = Borrower
    template_name = ".html"
    success_url = 


class BorrowerUpdateView(UpdateView):
    model = Borrower
    form_class = BorrowerForm
    template_name = ".html"
    success_url = 


class BorrowerDeleteView(DeleteView):
    model = Borrower
    form_class = BorrowerForm
    template_name = ".html"
    success_url = 
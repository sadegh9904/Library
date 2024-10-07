from django.shortcuts import render
from django.views import views
from django.views.generic import ListView,UpdateView,DeleteView
from django.views.generic.edit import CreateView
# Create your views here.


class ModelListView(ListView):
    model = Model
    template_name = ".html"

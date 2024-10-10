from django.urls import path
from .import views

urlpatterns = [
    path("",views.BookListView.as_view(), name="book-list"),
    path("add",views.BookCreateView.as_view(),name="add-book"),
    path("edit/<int:pk>",views.BookUpdateView.as_view(),name="edit-book"),
    path("delete/<int:pk>",views.BookDeleteView.as_view(),name="delete-book")
]

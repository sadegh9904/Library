from django.urls import path
from .import views
from . views import SignupView,LoginView,LogoutView,ProfileUser,Return_book



urlpatterns = [
    path("",views.BookListView.as_view(), name="book-list"),
    path("add/",views.BookCreateView.as_view(),name="add-book"),
    path("edit/<int:pk>",views.BookUpdateView.as_view(),name="edit-book"),
    path("delete/<int:pk>",views.BookDeleteView.as_view(),name="delete-book"),
    path("borrow/<int:pk>/",views.borrow_book, name="book-borrow"),
    path("return-book/<int:pk>",Return_book, name="return-book"),
    path("profile/",ProfileUser, name="profile-user"),
    path("signup/", SignupView, name="signup"),
    path("login/", LoginView, name="login"),
    path("logout/", LogoutView, name="logout"),
]

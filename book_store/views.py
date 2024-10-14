from django.shortcuts import render,redirect,get_object_or_404, HttpResponse
from django.views import View
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.views.generic import ListView,UpdateView,DeleteView,View
from django.views.generic.edit import CreateView
from .models import User,Book,Borrow
from .forms import BookForm,UserForm,BorrowForm
from django.contrib.auth import authenticate, login, get_user,logout
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
# Create your views here.


class BookListView(ListView):
    model = Book
    template_name = "book_store/book-list.html"
    context_object_name = "books"


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = "book_store/book-create.html"
    success_url = reverse_lazy("book-list")

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = "book_store/book-create.html"
    success_url = reverse_lazy("book-list")


class BookDeleteView(DeleteView):
    model = Book
    template_name = "book_store/book-delete.html"
    success_url = reverse_lazy("book-list")





class UserprofileView(ListView):
    model = User
    template_name = ".html"


def borrow_book(request, pk):

    book = get_object_or_404(Book,pk=pk)
    if request.method == "POST":
        form = BorrowForm(request.POST)
        if form.is_valid() and book.is_available:
            borrow = form.save(commit=False)

            borrow.book = book
            borrow.user = request.user

            borrow.borrow_date = timezone.now()
            borrow.return_date = timezone.now() + timezone.timedelta(days=10)
            borrow.save()
            book.is_available == False
            book.save()
            return redirect("book-list")
        else :
            raise ValidationError("the book isn't available now")
    
    else :
        form = BorrowForm()

    return render(request , "book_store/book-borrow.html" ,{
        "form":form,
        "book":book,
        "is_available":book.is_available
    })


#class BorrowBookView(CreateView):
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
    
#class LoginLPageView(View):
    template_name = "book_store/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("book-list")

    def get(self, request):
        form = LoginForm()
        return render(request, "book_store/login.html",{
            "form":form
        })

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data["username"],
                password = form.cleaned_data["password"],
            )

            if user is not None:
                login(request, user)
                return redirect("book-list")
        
        return render(request, "book_store/login.html",{
            "form":form
        })

    #new i have to delete that view for login and add this one to the urls and see the end
#class LoginPageView(LoginView):
    template_name = "book_store/login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy("book-list")

    def form_invalid(self, form):
        messages.error(self.request, "invalid username or pass")
        return self.render_to_response(self.get_context_data(form=form))
    

def SignupView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("book-list")
        return render(request, "book_store/signup.html", {
            "form":form
        })
    
    form = UserCreationForm()

    return render(request, "book_store/signup.html", {
        "form":form
    })


def LoginView(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("book-list")

    form = AuthenticationForm()
    return render(request, "book_store/login.html", {
        "form":form
    })

def LogoutView(request):
    if request.method == "POST":
        logout(request)
        return redirect("book-list")
from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=254)
    balance = models.IntegerField(default=0)

    def __str__(self):
        
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, db_index=True,editable=False)

    def __str__(self):
        return self.title




class Borrow(models.Model):
    user = models.ForeignKey(User, verbose_name=("user"), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, verbose_name=("book"), on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.name} borrowed {self.book.title}"
from django.db import models

# Create your models here.


class Borrower(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=254)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, db_index=True)
    borrowed_books = models.ForeignKey(Borrower, verbose_name=("borrowed_books"), on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.title


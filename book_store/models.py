from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import datetime
from django.template.defaultfilters import slugify #for error adding book , we must make sure that the slug isn't duplicated!
# Create your models here.

class CustomUser(AbstractUser):
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.username



class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, db_index=True,editable=False)

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title




class Borrow(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name=("user"), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, verbose_name=("book"), on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.name} borrowed {self.book.title}"
    
    def return_book(self):
        self.return_date = timezone.now()
        self.save()

    def calculate_late(self):
        if self.return_date:
            borrow_days = (self.return_date - self.borrow_date).days
            late_days = borrow_days - 10 

            if late_days > 0 :
                self.user.balance -= late_days
                self.user.save()



from django.contrib.auth.models import User
from django.db import models
from bookapp.models import Book

class Cart(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    items=models.ManyToManyField(Book)

class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    BOOK = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

from django.db import models
from api.category.models import Category

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    is_available = models.BooleanField(blank=True, default=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

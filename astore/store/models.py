from django.db import models
from django.db.models import Model
from django.urls import reverse


class Category(Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def get_absolute_url(self):
        return reverse(
            'store:product-list-by-category',
            args = [
                self.slug
            ]
            # kwargs = {
            #     'pk': self.pk
            # }
        )
    
    
    def __str__(self):
        return f'{self.name}'


class Product(Model):
    category = models.ForeignKey(
        'store.Category',
        on_delete=models.CASCADE,
        related_name='products'
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return reverse(
            'store:product-detail',
            args = [
                self.id,
                self.slug
            ]
            # kwargs = {
            #     'pk': self.pk
            # }
        )
    
    
    def __str__(self):
        return f'{self.name}'
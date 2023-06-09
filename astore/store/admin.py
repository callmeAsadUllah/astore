from django.contrib import admin
from django.contrib.admin import ModelAdmin


from store.models import (
    Category,
    Product
)


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = [
        'name', 
        'slug'
    ]
    prepopulated_fields = {
        'slug': [
            'name'
        ]
    }
 
 
@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = [
        'id',
        'name',
        'slug',
        'price',
        'available',
        'created',
        'updated'
    ]
    list_filter = [
        'available',
        'created',
        'updated'
    ]
    list_editable = [
        'price',
        'available'
    ]
    prepopulated_fields = {
        'slug': [
            'name'
        ]
    }

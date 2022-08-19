from django.contrib import admin
from .models import Products

# Register your models here.
@admin.register(Products)
class ProductModel(admin.ModelAdmin):
    list_display = ('name','cost','owner')
    search_fields = ('name','category')


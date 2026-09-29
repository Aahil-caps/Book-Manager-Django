from django.contrib import admin
from books.models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','price','published_date','is_available')
    search_fields = ('title','author')
    ordering = ("-published_date",)
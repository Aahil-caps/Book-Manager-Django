from django.urls import path
from . import views

urlpatterns = [
    path('book_list/',views.book_list,name='book_list'),
    path('book_create/',views.book_create,name='book_create')
]
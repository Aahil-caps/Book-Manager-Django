from django.shortcuts import render,redirect
from .models import Book

def book_list(request):
    ordering = Book.objects.all().order_by("-published_date")
    return render(request,'book_list.html',{'books':ordering}) 


def book_create(request):
    if request.method == 'POST':
        title = request.POST.get('title','')
        author = request.POST.get('author','')
        price = request.POST.get('price', 0)
        published_date = request.POST.get('published_date','')

        if not title:
            return render(request, 'book_form.html', {
        'error': 'Title cannot be empty'
    })

        Book.objects.create(title=title,author=author,price=price,published_date=published_date)
        return redirect('book_list')
    return render(request,'book_form.html')
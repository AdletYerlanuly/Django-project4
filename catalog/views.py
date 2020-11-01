from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
# Create your views here.
def index(request):
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  

    return render(
        request,
        'index.html',
        context = {'num_books':num_books,
        'num_instances':num_instances,
        'num_instances_available':num_instances_available,
        'num_authors':num_authors},
    )

def books(request):
	book_list=Book.objects.all()
	return render(request, 'catalog/books.html', {
		'book_list': book_list
	})

def book_details(request, id):
	book=Book.objects.get(id=id)
	return render(request, 'catalog/book_detail.html', {
		'book': book
	})
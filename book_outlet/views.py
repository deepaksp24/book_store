from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import Book
from django.db.models import Avg, Max, Min

# Create your views here.


def index(request):
    books = Book.objects.all().order_by("-title")
    num_books = books.count()
    avg_books = books.aggregate(Avg("rating"))
    return render(request, "book_outlet/index.html", {
        "books": books,
        "total_number_of_books": num_books,
        "avaerage_rating": avg_books
    })


def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()

    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling,

    })

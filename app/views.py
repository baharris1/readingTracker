from django.shortcuts import render, redirect
from .models import Book, Update
from .forms import BookForm


# Create your views here.
def home(request):
    form = BookForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            book = form.save()
            book.save()
            return redirect("app:home")

    books = Book.objects.values()

    return render(request, 'app/home.html', {"form": form,
                                             "books": books}
                  )

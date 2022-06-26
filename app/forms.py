from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    title = forms.CharField(label='Book Title', max_length=200)
    author = forms.CharField(label='Written By', max_length=200)
    pages = forms.IntegerField(label='Pages')

    class Meta:
        model = Book
        exclude = (' ', )

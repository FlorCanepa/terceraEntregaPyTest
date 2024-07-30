from django import forms
from .models import Author, Book, Publisher

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'publication_date', 'author']

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'address']

class SearchForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)

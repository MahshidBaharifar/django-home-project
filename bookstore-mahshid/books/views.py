from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import Book,Review
from django.views.generic import ListView, DetailView, CreateView, DeleteView

# Create your views here.

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Review
    template_name= 'book_details.html'
    context_object_name = 'review'

class BookCreateView(CreateView):
    model = Book
    fields=["title","author","description"]
    template_name= 'book_create.html'
    success_url= reverse_lazy("book-list")

   # def form_valid(self, form: BaseModelForm) :
   #     self.object = form.save()
   #     return redirect(self.success_url())

class BookDeleteView(DeleteView):
    model = Book
    template_name = "book_delete.html"
    success_url = reverse_lazy("book-list")


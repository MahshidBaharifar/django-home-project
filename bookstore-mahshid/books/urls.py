from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView , BookDeleteView

urlpatterns = [
    path("",BookListView.as_view(), name='book-list' ),
    path("<int:pk>/", BookDetailView.as_view(),name= 'book-detail'),
    path("create/", BookCreateView.as_view(),name='book-create'),
    path("<int:pk>/delete/", BookDeleteView.as_view(), name='book-delete'  ),

]
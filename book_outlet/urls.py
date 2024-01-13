from django.urls import path
from . import views

urlpatterns = [
    path('', views.index)
]


# http://localhost:8000/ ---> render book homepage
# http://localhost:8000/books ---> render all-books page
# http://localhost:8000/books/detailed_book ---> render detailed_books page

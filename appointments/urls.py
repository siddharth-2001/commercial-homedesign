from django.urls import path
from .views import book_appointment

urlpatterns = [
    path('book-appointment', book_appointment, name = 'book-app'),
]
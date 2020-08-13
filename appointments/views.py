from django.shortcuts import render
from django.views import generic
from .models import Appointment
from django.http import HttpResponse
from .models import Appointment

# Create your views here.

def book_appointment(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    return render(request,'appointment.html')


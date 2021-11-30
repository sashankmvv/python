from django.shortcuts import render
from django.http import HttpResponseRedirect, request

def contact(request):
    return render(request,'ngo/contactus.html')

def home(request):
    return render(request, 'ngo/home.html')
from .models import Ngo
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NgoSignUpForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from eventManager.models import PostEvent

# Create your views here.


def ngo_register(request):
    if request.method == 'POST':
        form = NgoSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('home')
    else:
        form = NgoSignUpForm()
    return render(request, 'ngo/register.html', {'form': form})

def ngo_login(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'ngo/login.html',
    context={'form':AuthenticationForm()})

def eventlist(request):
    event = PostEvent.objects.all()
    return render(request, 'ngo/eventList.html', {'events':event})

def eventDetail(request, pk):
    obj = PostEvent.objects.filter(id=pk)
    return render(request, 'ngo/eventDetail.html', {'event':obj[0]})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('ngo-profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        ob = Ngo.objects.filter(user= request.user)
    context = {
        'form': u_form,
        'event': ob[0]
    }

    return render(request, 'ngo/profile.html', context)
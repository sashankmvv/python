from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, request
from .forms import EventManagerSignUpForm, UserUpdateForm, EventUpdateForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView
from .models import PostEvent
from ngo.models import EventManager

class PostCreateView(LoginRequiredMixin, CreateView):
    model = PostEvent
    fields = ['event_name', 'event_type', 'event_manager','event_contact', 'event_address', 'event_location', 'event_city', 'event_state', 'event_zipcode', 'event_foodqty']
    
    def form_valid(self, form):
        if self.request.user.is_eventManager:
            obj = EventManager.objects.filter(user=self.request.user)
            form.instance.event_organiser = obj[0]
            form.instance.event_status = True
            return super().form_valid(form)
        else:
            return redirect('event-login')


def myPost(request):
    events = PostEvent.objects.filter(event_organiser = request.user.id)
    return render(request, 'eventManager/myPost.html', {'events':events})

# Create your views here.
def home(request):
    return render(request, 'eventManager/home.html')

def organizer_register(request):
    if request.method == 'POST':
        form = EventManagerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event-home')
    else:
        form = EventManagerSignUpForm()
    return render(request, 'eventManager/register.html', {'form': form})

def organizer_login(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('event-profile')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'eventManager/login.html',
    context={'form':AuthenticationForm()})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        
        if u_form.is_valid():
            u_form.save()
            return redirect('event-profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        ob = EventManager.objects.filter(user= request.user)
    context = {
        'form': u_form,
        'event': ob[0]
    }

    return render(request, 'eventManager/profile.html', context)


@login_required
def event_update(request, pk): 
    instance = get_object_or_404(PostEvent, id=pk)
    form = EventUpdateForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('event-myevents')
    return render(request, 'eventManager/updateEvent.html', {'form': form})
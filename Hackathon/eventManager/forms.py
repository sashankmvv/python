from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from ngo.models import User, EventManager
from .models import PostEvent


class EventManagerSignUpForm(UserCreationForm):
    Organization_name = forms.CharField(required=True)
    manager_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField(required=True)
    zipcode = forms.CharField(required=True)
    state = forms.CharField(required=True)
    city = forms.CharField(required=True)
    organisation_picture = forms.ImageField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_eventManager = True
        user.name = self.cleaned_data.get('Organization_name')
        user.manager_name = self.cleaned_data.get('manager_name')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.email = self.cleaned_data.get('email')
        user.address = self.cleaned_data.get('address')
        user.zipcode = self.cleaned_data.get('zipcode')
        user.state = self.cleaned_data.get('state')
        user.city = self.cleaned_data.get('city')
        user.save()
        event_manager = EventManager.objects.create(user=user)
        EventManager.organisation_picture = self.cleaned_data.get('Organisation_picture')
        event_manager.save()
        return user


class UserUpdateForm(forms.ModelForm):
    name = forms.CharField()
    manager_name = forms.CharField()
    phone_number = forms.CharField()
    email = forms.EmailField()
    address = forms.CharField()
    zipcode = forms.CharField()
    state = forms.CharField()
    city = forms.CharField()
    organisation_picture = forms.ImageField(required=False)

    class Meta:
        model = EventManager
        fields = ['name', 'manager_name', 'email', 'phone_number',
                  'address', 'state', 'city', 'zipcode', 'organisation_picture']


class EventUpdateForm(forms.ModelForm):
    event_name = forms.CharField()
    event_manager = forms.CharField()
    event_contact = forms.CharField()
    event_address = forms.CharField()
    event_location = forms.CharField()
    event_city = forms.CharField()
    event_state = forms.CharField()
    event_zipcode = forms.CharField()
    event_foodqty = forms.IntegerField()
    event_type = forms.CharField()
    event_status = forms.BooleanField(required=False)

    class Meta:
        model = PostEvent
        fields = ['event_name', 'event_type', 'event_manager', 'event_contact', 'event_address',
                  'event_location', 'event_city', 'event_state', 'event_zipcode', 'event_foodqty', 'event_status']

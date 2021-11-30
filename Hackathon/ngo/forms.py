from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User, Ngo

class NgoSignUpForm(UserCreationForm):
    NGO_name = forms.CharField(required=True)
    manager_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField(required=True)   
    state = forms.CharField(required=True) 
    city = forms.CharField(required=True)
    zipcode = forms.CharField(required=True)
    

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_ngo = True
        user.name = self.cleaned_data.get('NGO_name')
        user.manager_name = self.cleaned_data.get('manager_name')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.email = self.cleaned_data.get('email')
        user.address = self.cleaned_data.get('address')
        user.zipcode = self.cleaned_data.get('zipcode')
        user.state = self.cleaned_data.get('state')
        user.city = self.cleaned_data.get('city')
        user.save()
        ngo = Ngo.objects.create(user=user)
        ngo.save()
        return user


class UserUpdateForm(forms.ModelForm):
    name = forms.CharField()
    manager_name = forms.CharField()
    phone_number = forms.CharField()
    email = forms.EmailField()
    address = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    zipcode = forms.CharField()

    class Meta:
        model = Ngo
        fields = ['name', 'email', 'manager_name','phone_number','address','zipcode','state','city']
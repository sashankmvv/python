from django.db import models
from django.contrib.auth.models import AbstractUser, User
from PIL import Image

# Create your models here.


class User(AbstractUser):
    is_ngo = models.BooleanField('ngo status', default=False)
    is_eventManager = models.BooleanField('eventManager status', default=False)
    name = models.CharField(max_length=50,default=' ')
    manager_name = models.CharField(max_length=50,default=' ')
    phone_number = models.CharField(max_length=12,default=' ')
    email = models.EmailField(default='')
    address = models.TextField(default=' ')  
    state = models.CharField(max_length=50,default=' ') 
    city = models.CharField(max_length=50,default=' ')
    zipcode = models.CharField(max_length=10)

class Ngo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True) 

    def __str__(self):
        return self.user.username

class EventManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    organisation_picture = models.ImageField(default='default.jpg', upload_to='organisation_pics',null=True, blank=True)

    
    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.organisation_picture.path)
        if img.height > 250 or img.width > 250:
            output_size=(250,250)
            img.thumbnail(output_size)
            img.save(self.organisation_picture.path)

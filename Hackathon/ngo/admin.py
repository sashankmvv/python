from django.contrib import admin
from .models import Ngo, EventManager, User
# Register your models here.

admin.site.register(Ngo)
admin.site.register(EventManager)
admin.site.register(User)
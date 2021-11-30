from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='event-home'), 
    path('register/', views.organizer_register, name='event-register'), 
    path('login/', views.organizer_login, name='event-login'),
    path('profile/', views.profile, name='event-profile'),
    path('myevents/', views.myPost, name='event-myevents'),
    path('updateEvent/<int:pk>', views.event_update, name='event-update'),
    path('create/', views.PostCreateView.as_view(),name='new-event'),
    path('logout/',auth_views.LogoutView.as_view(template_name='eventManager/logout.html'),name="event-logout"), 
]
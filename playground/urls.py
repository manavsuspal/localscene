from django.urls import path 
from . import views 
from playground.models import *

urlpatterns = [
    path('login/', views.login),
    path('home/',views.home),
    path('event/',views.event_page),
    path('signup/',views.signup),
]


for obj in Event.objects.all():
    urlpatterns.append(path(obj.slug, views.event_page))


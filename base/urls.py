from . import views
from django.urls import path

urlpatterns = [
    # This is where the urls linking to other pages takes place
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
]

from . import views
from django.urls import path

urlpatterns = [
    # This is where the urls linking to other pages takes place
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('menu/', views.menu, name = 'menu'),
    path('book_table/', views.book_table, name = 'book_table'),
    path('chefs/', views.chefs, name = 'chefs'),
    path('event/', views.event, name = 'event'),
    path('dishes/', views.dishes, name = 'dishes'),
    path('career/', views.career, name = 'career'),
    path('press/', views.press, name = 'press'),
    path('blog/', views.blog, name = 'blog'),
]

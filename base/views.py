from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def menu(request):
    return render(request, 'menu.html')

def book_table(request):
    return render(request, 'book_table.html')

def chefs(request):
    return render(request, 'chefs.html')

def event(request):
    return render(request, 'event.html')

def dishes(request):
    return render(request, 'dishes.html')

def career(request):
    return render(request, 'career.html')

def press(request):
    return render(request, 'press.html')

def blog(request):
    return render(request, 'blog.html')
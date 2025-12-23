from django.shortcuts import render

def home(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, "about.html")

def departments(request):
    return render(request, "departments.html")

def insurance(request):
    return render(request, 'insurance.html') 
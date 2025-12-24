from django.shortcuts import render

def home(request):
    return render(request, 'Nav-tab/index.html')


def contact(request):
    return render(request, 'Nav-tab/contact.html')


def about(request):
    return render(request, "Nav-tab/about.html")

def departments(request):
    return render(request, "Nav-tab/departments.html")

def insurance(request):
    return render(request, 'Nav-tab/insurance.html') 

def cardiology(request):
    return render(request,'Departments/cardiology.html')

def neurology(request):
    return render(request,'Departments/neurology.html')

def orthopaedics(request):
    return render(request,'Departments/orthopaedics.html')
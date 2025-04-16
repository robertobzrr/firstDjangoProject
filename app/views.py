from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "index.html")

def categoriesPage(request):
    return render(request, "categoriesPage.html")

def listPage(request):
    return render(request, "listPage.html")


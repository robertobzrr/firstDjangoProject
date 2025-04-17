from django.shortcuts import render
from django.http import HttpResponse


def home(request):


    list_itens = [

        {
            "id" : "01",
            "name" : "Beef",
            "category" : "Meat",
        },

        {
            "id" : "02",
            "name" : "Pork",
            "category" : "Meat",
        }

    ]
    context = {"list": list_itens}
    #name = "roberto"
    #context = {"first_name": name}
    return render(request, "index.html", context=context) #, context=context (dentro do ()))



def categoriesPage(request):
    return render(request, "categoriesPage.html")



def listPage(request):
    return render(request, "listPage.html")


from django.urls import path
from . import views

urlpatterns = [

    path("", views.home),
    path("categoriesPage", views.categoriesPage),
    path("listPage", views.listPage),

]
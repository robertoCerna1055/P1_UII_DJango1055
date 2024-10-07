from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.indexvista, name="indexvista"),
    path('mama/', views.mi_mama, name="mama.html")
]
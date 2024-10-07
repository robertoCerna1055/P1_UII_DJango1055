from django.shortcuts import render

# Create your views here.

def indexvista(request):
    return render(request,'index.html')

def mi_mama(request):
    return render(request,'mama.html')


from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello Pickleballers!</h1>')

def about(request):
    return render(request, 'about.html')

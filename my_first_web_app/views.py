from django.http import HttpResponse
from random import randint
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect

from my_first_web_app.views import home_page,portfolio_page,about_me

def root(request):
    return HttpResponseRedirect('home')
def home_page(request):
     response = render(request, 'index.html')
     return HttpResponse(response)

def portfolio_page(request):
     response = render(request, 'gallery.html')
     return HttpResponse(response)
     random_number = randint(0,100)
     image_url = "https://picsum.photos/400/600/?image={}".format(random_number)
     context = {'gallery_image': image_url}
     response = render(request, 'gallery.html', context)
     return HttpResponse(response)

def about_me(request):
     response = render(request, 'about.html')
     return HttpResponse(response)

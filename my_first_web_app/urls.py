"""my_first_web_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.http import HttpResponse
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
from random import randint
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path

from my_first_web_app.views import root, home_page,portfolio_page,about_me
urlpatterns = [
     path('', root),
     path('home/', home_page),
     path('portfolio/', portfolio_page),
     path('about/', about_me)
]

image_urls = []
for i in range(5):
   random_number = randint(0,100)
   image_urls.append("https://picsum.photos/400/600/?image={}".format(random_number))

context = {'gallery_images': image_urls}
response = render(request, 'gallery.html', context)
return HttpResponse(response)

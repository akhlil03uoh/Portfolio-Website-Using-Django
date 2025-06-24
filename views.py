from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def Base(request):
    template = loader.get_template('Base.html')
    return HttpResponse(template.render())

def Home(request):
    template = loader.get_template('Home.html')
    return HttpResponse(template.render())

def About(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def Projects(request):
    template = loader.get_template('Projects.html')
    return HttpResponse(template.render())

def Resume(request):
    template = loader.get_template('Resume.html')
    return HttpResponse(template.render())

def Contact(request):
    template = loader.get_template('Contact.html')
    return HttpResponse(template.render())

def home(request):
    return render(request, 'webApp/home.html')


# Create your views here.

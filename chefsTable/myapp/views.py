from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from myapp.forms import InputForm

def home(request):
    return HttpResponse("Hello World!")

def pathview(request, name, id): 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 

def qryview(request): 
    name = request.GET['name'] 
    id = request.GET['id'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 

def showform(request): 
    return render(request, "form.html") 

def form_view(request):
    form = InputForm()
    context = {"form": form}
    return render(request, "home.html", context)
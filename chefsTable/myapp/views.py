from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from myapp.forms import InputForm, LogForm

def home(request):
    return HttpResponse("Hello World!")

def pathview(request, name, id): 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 

def qryview(request): 
    name = request.GET['name'] 
    id = request.GET['id'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 

def showform(request): 
    context = {'nums':[1,2,3,4], 'name':'Harry porter'}
    return render(request, "form.html", context) 

def form_view(request):
    form = LogForm()
    if request.method == "POST":
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "home.html", context)

def about(request):
    about_context = {'about': "Based in Chicago"}
    return render(request, "about.html", about_context)

from .models import Menu
def menu_by_id(request):
    newmenu = Menu.objects.all()
    newmenu_dic = {'menu':newmenu}
    return render(request,'menu_cards.html',newmenu_dic)

def index(request):
    return render(request, 'index.html')
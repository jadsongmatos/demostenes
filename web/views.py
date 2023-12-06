from django.http import HttpResponse
from django.template import loader


from django.views.generic.edit import UpdateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import LoginForm
from .models import Product

#from .models import Pagamentos

#from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from .forms import UserCreationWithEmailForm

class SignUpView(generic.CreateView):
    form_class = UserCreationWithEmailForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def home(request):
    template = loader.get_template('home.html')
    context = {}
    return HttpResponse(template.render(context, request))

def profile(request):
    template = loader.get_template('profile.html')
    context = {
        'nome':  'user.first_name',
        'sobrenome': 'user.last_name'
    }
    return HttpResponse(template.render(context, request))

def products(request):
    products = Product.objects.all().values()
    template = loader.get_template('all_members.html')
    print("products", len(products))
    context = {
        'products': products,
    }
    return HttpResponse(template.render(context, request))

     
def listPagamento(request): 
    template = loader.get_template('profile.html')
    listPagamento = Pagamentos.objects.all()
    return render(request, 'profile.html', {'pagamentos': Pagamentos})
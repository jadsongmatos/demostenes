from django.http import HttpResponse
from django.template import loader
from .models import Product

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.models import User

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(email = form.cleaned_data.get('email'))
                password = form.cleaned_data.get('password')
                user = authenticate(request,username=user.username, password=password)
                print("----is_valid",user)
                if user is not None:
                    login(request, user)

                    return redirect('home')  # Redirecione para a página desejada
            except:
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def home(request):
    template = loader.get_template('home.html')
    context = {}
    return HttpResponse(template.render(context, request))

def home(request):
    template = loader.get_template('home.html')
    context = {}
    return HttpResponse(template.render(context, request))

def products(request):
    products = Product.objects.all().values()
    template = loader.get_template('all_members.html')
    print("products", len(products))
    context = {
        'products': products,
    }
    return HttpResponse(template.render(context, request))

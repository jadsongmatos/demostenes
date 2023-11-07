from django.http import HttpResponse
from django.template import loader
from .models import Product

def login(request):
    template = loader.get_template('login.html')
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

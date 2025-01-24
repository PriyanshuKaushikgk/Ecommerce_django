from django.shortcuts import HttpResponse
from django.shortcuts import render
from store.models import Product

# Create your views here.

def home(request):
    products = Product.objects.filter(is_available=True)
    context = {
        'products':products
    }
    return render(request,'index.html',context)
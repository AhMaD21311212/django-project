from django.shortcuts import render
from django.views.generic import TemplateView
from product.models import product

# Create your views here.


def productView(request):
    Product = product.objects.all()
    recent_product = product.objects.all()[:3]

    return render(request,'home/index.html',{"product":Product, "recent":recent_product})




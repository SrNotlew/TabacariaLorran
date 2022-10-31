from re import template
from django.shortcuts import render
from .models import Produto

# Create your views here.

def produto_list(request):
    template_name='produtos_list.html'
    objects=Produto.objects.all()
    context={'object_list': objects}
    return render(request,template_name, context)

def produto_detail(request,pk):
    template_name='produtos_detail.html'
    obj = Produto.objects.get(pk=pk)
    context={'object': obj}
    return render(request,template_name, context)
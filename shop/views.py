from django.shortcuts import render
from .models import Producto


def lista_productos(request):
    productos = Producto.objects.all().order_by("nombre")
    return render(request, "productos.html", {"productos": productos})

# Create your views here.

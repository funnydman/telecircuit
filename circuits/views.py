from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.apps import apps
from orders.forms import ContactForm

def circuits(request):
    return render(request, 'circuits.html', {})


def get_circuits_list(request, brand):
    brand = apps.get_model('circuits', brand.title())
    models = brand.objects.all()
    return render(request, 'circuits.html', {"models": models})

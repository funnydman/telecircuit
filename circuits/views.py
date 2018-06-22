from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.apps import apps
from orders.forms import ContactForm

def circuits(request):
    return render(request, 'circuits.html', {})


def get_circuits_list(request, brand):
    brand = apps.get_model('circuits', brand.title())
    models = brand.objects.all()

    paginator = Paginator(models, 5)  # Show 5 pag_items per page

    page = request.GET.get('page')
    try:
        models_per_page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        models_per_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        models_per_page = paginator.page(paginator.num_pages)

    return render(request, 'circuits.html', {"models": models, "models_per_page": models_per_page})


def get_query_set_from_search(request):
    pass
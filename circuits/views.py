from django.apps import apps
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect

from orders.forms import ContactForm
from .models import Samsung, Lg, Horizont, Vityaz, Philips
from .utils import get_queryset_from_search, get_queryset_from_one_model_search


def handle_contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('circuits')
    else:
        form = ContactForm()
    return form


def circuits(request):
    brands_list = [Samsung, Lg, Horizont, Vityaz, Philips]
    query = request.GET.get("search")
    models_per_page = []
    if query:
        models_per_page = get_queryset_from_search(brands_list, query)

    form = handle_contact_form(request)
    return render(request, 'circuits.html',
                  {"models_per_page": models_per_page, "form": form})


def get_circuits_list(request, brand):
    brand = apps.get_model('circuits', brand.title())
    models = brand.objects.all()
    query = request.GET.get("search")
    if query:
        models = get_queryset_from_one_model_search(brand, query)
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

    form = handle_contact_form(request)
    return render(request, 'circuits.html',
                  {"models_per_page": models_per_page,
                   "brand": str(brand.__name__), "form": form})

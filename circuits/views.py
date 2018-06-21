from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect

from orders.forms import ContactForm
from .models import Samsung


def get_circuits_list(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            form.save()
            return redirect('circuits-list')
    else:
        form = ContactForm()

    models_of_brand = Samsung.objects.all()

    paginator = Paginator(models_of_brand, 3)  # Show 3 pag_items per page

    page = request.GET.get('page')
    try:
        pag_items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pag_items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pag_items = paginator.page(paginator.num_pages)
    return render(request, 'circuits.html',
                  {'models_of_brand': models_of_brand, 'pag_items': pag_items,
                   'form': form})

from itertools import chain

from django.db.models import Q


def get_queryset_from_one_model_search(brand, query):
    search_query = brand.objects.all().filter(
        Q(model__icontains=query) |
        Q(power__icontains=query) |
        Q(main__icontains=query) |
        Q(t_con__icontains=query) |
        Q(x_main__icontains=query) |
        Q(y_main__icontains=query) |
        Q(logic__icontains=query) |
        Q(inverter__icontains=query) |
        Q(y_skan__icontains=query)
    ).distinct()
    return search_query or []


def get_queryset_from_search(brands_list, query):
    query_search_result = []
    for brand in brands_list:
        search_query = get_queryset_from_one_model_search(brand, query)
        if search_query:
            query_search_result.append(search_query)
    return list(chain(*query_search_result)) or []

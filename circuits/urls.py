from django.urls import path

from . import views

urlpatterns = [
    path('circuits/', views.get_circuits_list, name='circuits-list')
]

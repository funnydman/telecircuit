from django.urls import path

from . import views

urlpatterns = [
    path('circuits/', views.circuits, name='circuits'),
    path('circuits/<str:brand>/', views.get_circuits_list, name="circuits-list")
]

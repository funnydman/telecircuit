from django.contrib import admin

from .models import Samsung, Lg, Horizont, Vityaz, Philips


@admin.register(Samsung, Lg, Horizont, Vityaz, Philips)
class InlineBrand(admin.ModelAdmin):
    list_display = (
        'model', 'power', 'main', 't_con', 'x_main', 'y_main', 'logic',
        'inverter',
        'y_skan', 'other')

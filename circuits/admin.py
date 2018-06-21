from django.contrib import admin

from .models import Samsung, LG, Horizont, Vityaz, Philips, Toshiba, Sony, \
    Panasonic, Dell


@admin.register(Samsung, LG, Horizont, Vityaz, Philips, Toshiba, Sony,
                Panasonic, Dell)
class InlineBrand(admin.ModelAdmin):
    list_display = (
        'model', 'power', 'main', 't_con', 'x_main', 'y_main', 'logic',
        'inverter',
        'y_skan', 'other')

from django.db import models


class Brand(models.Model):
    model = models.CharField(max_length=250)
    power = models.CharField(max_length=250, blank=True)
    main = models.CharField(max_length=250, blank=True)
    t_con = models.CharField(max_length=250, blank=True)
    x_main = models.CharField(max_length=250, blank=True)
    y_main = models.CharField(max_length=250, blank=True)
    logic = models.CharField(max_length=250, blank=True)
    inverter = models.CharField(max_length=250, blank=True)
    y_skan = models.CharField(max_length=250, blank=True)
    other = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.model

    class Meta:
        abstract = True


class Samsung(Brand):
    class Meta:
        verbose_name_plural = "Samsung"


class LG(Brand):
    class Meta:
        verbose_name_plural = "LG"


class Horizont(Brand):
    class Meta:
        verbose_name_plural = "Horizont"


class Vityaz(Brand):
    class Meta:
        verbose_name_plural = "Vityaz"


class Philips(Brand):
    class Meta:
        verbose_name_plural = "Philips"


class Toshiba(Brand):
    class Meta:
        verbose_name_plural = "Toshiba"


class Sony(Brand):
    class Meta:
        verbose_name_plural = "Sony"


class Panasonic(Brand):
    class Meta:
        verbose_name_plural = "Panasonic"


class Dell(Brand):
    class Meta:
        verbose_name_plural = "Dell"

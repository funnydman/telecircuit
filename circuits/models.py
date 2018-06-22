from django.db import models


class Brand(models.Model):
    model = models.CharField(max_length=250, unique=True)
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


class Lg(Brand):
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

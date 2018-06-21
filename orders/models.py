from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=50, blank=False)
    message = models.TextField(blank=False)

    def __str__(self):
        return self.email

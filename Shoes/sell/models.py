from django.db import models
from django.urls import reverse

# Create your models here


class Shoe(models.Model):

    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sell:detail', kwargs={'pk': self.pk})






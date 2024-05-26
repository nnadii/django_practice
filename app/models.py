from django.db import models

# Create your models here.


class Monthly(models.Model):

    def __str__(self):
        return self.january

    january = models.CharField(max_length=100)
    febuary = models.CharField(max_length=100)
    march = models.CharField(max_length=100)
    april = models.CharField(max_length=100)
    may = models.CharField(max_length=100)
    june = models.CharField(max_length=100)
    july = models.CharField(max_length=100)
    august = models.CharField(max_length=100)
    september = models.CharField(max_length=100)
    october = models.CharField(max_length=100)
    november = models.CharField(max_length=100)
    december = models.CharField(max_length=100)

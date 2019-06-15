from django.db import models

# Create your models here.


class Pizza(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return '{} -- {} -- {}'.format(self.name, self.description, self.price)


class Order(models.Model):
    date = models.DateTimeField(auto_now=True)
    pizzas = models.ManyToManyField(Pizza)

    def __str__(self):
        return self.date

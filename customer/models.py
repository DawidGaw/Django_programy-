from django.db import models


class Basket(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Basket {self.id}'

class Customer(models.Model):
    name = models.CharField(max_length=100)
    registration_date = models.DateField(auto_now_add=True)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


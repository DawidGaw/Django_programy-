from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Customer, Basket


@receiver(pre_save, sender=Customer)
def create_basket_for_customer(sender, instance, **kwargs):
    if not instance.basket_id:
        basket = Basket.objects.create()
        instance.basket = basket
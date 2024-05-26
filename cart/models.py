from django.db import models

from account.models import User
from product.models import product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Orders')
    total_price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.user.Phone




class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="Item")
    Product = models.ForeignKey(product,on_delete=models.CASCADE, related_name="Item")
    size = models.CharField(max_length=15)
    color = models.CharField(max_length=15)
    quantity = models.SmallIntegerField()
    price = models.PositiveIntegerField(null=True, blank=True)

class DiscountCode(models.Model):
    name = models.CharField(max_length=20, unique=True)
    discount = models.SmallIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.name







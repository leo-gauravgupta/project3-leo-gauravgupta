from django.db import models

# Create your models here.

class Topping(models.Model):
    topping = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.topping}"

class Menu(models.Model):
    item = models.CharField(max_length=64)
    subItem = models.CharField(max_length=64)
    toppings = models.ManyToManyField(Topping, blank=True, related_name="toppingsmenu")
    priceSmall = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    priceLarge = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Item: {self.item}, Sub-Item: {self.subItem}, Toppings: {self.toppings}, Price-Small: {self.priceSmall}, Price-Large: {self.priceLarge}"

class Order(models.Model):
    orderSizes = (
        ('Small', 'Small'),
        ('Large', 'Large')
    )
    order_item = models.CharField(max_length=64, blank=True, null=True)
    order_subItem = models.CharField(max_length=64, blank=True, null=True)
    order_toppings = models.CharField(max_length=64, blank=True, null=True)
    orderSize = models.CharField(max_length=10, choices=orderSizes)
    orderPrice = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    orderQty = models.IntegerField()
    orderCost = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.id} - Order-Item: {self.order_item}, Order-SubItem: {self.order_subItem}, Order-Toppings: {self.order_toppings}, Order-Size: {self.orderSize}, Order-Price: {self.orderPrice}, Order-Qty: {self.orderQty}, Order-Cost: {self.orderCost}"

class Customer(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    custUserID = models.CharField(max_length=64)
    orders = models.ManyToManyField(Order, blank=True, related_name="customerorders")

    def __str__(self):
        return f"{self.first} {self.last}"

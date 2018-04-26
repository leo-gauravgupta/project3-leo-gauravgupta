from django.contrib import admin

# Register your models here.

from .models import Topping, Menu, Order, Customer

# to display all columns on the admin site:
class MenuAdmin(admin.ModelAdmin):
    list_display = ('item', 'subItem', 'toppings', 'priceSmall', 'priceLarge')

    def item(self, obj):
        return obj.item

    def subItem(self, obj):
        return obj.subItem

    def toppings(self, obj):
        return obj.toppings

    def priceSmall(self, obj):
        return obj.priceSmall

    def priceLarge(self, obj):
        return obj.priceLarge

class CustomerInline(admin.StackedInline):
    model = Customer.orders.through
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    inlines = [CustomerInline]

class CustomerAdmin(admin.ModelAdmin):
    filter_horizontal = ("orders",)

admin.site.register(Topping)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Customer, CustomerAdmin)

from django.contrib import admin

from .models import OrderedsTransactions, Transaction, OrderItems, Category, Product, Location, Contact, Ordereds


# Register your models here.
admin.site.register(Location)
admin.site.register(Contact)
admin.site.register(Ordereds)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(OrderItems)
admin.site.register(Transaction)
admin.site.register(OrderedsTransactions)

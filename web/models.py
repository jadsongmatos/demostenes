from django.db import models
import uuid

from django.contrib.gis.db import models as gis_models
from django.contrib.auth.models import User

class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address = models.CharField(max_length=255, blank=True, null=True)
    coordinates = gis_models.PointField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    nation = models.CharField(max_length=255)
    auth_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="locations")

class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=255, null=False, blank=False)
    contact = models.CharField(max_length=255, null=False, blank=False)
    auth_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="locations")


class Ordereds(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    create_time = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now=True)
    status = models.CharField(max_length=1)
    auth_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="locations")

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=1, null=True, blank=True)
    price = models.PositiveSmallIntegerField(null=True, blank=True)
    stock = models.PositiveSmallIntegerField(null=True, blank=True)
    id_category = models.UUIDField(null=True, blank=True)

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
    
class OrderItems(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    length = models.SmallIntegerField(null=True, blank=True)
    price = models.SmallIntegerField(null=True, blank=True)
    discount = models.SmallIntegerField(null=True, blank=True)
    rate = models.SmallIntegerField(null=True, blank=True)
    id_ordereds = models.UUIDField(null=True, blank=True)
    id_products = models.UUIDField(null=True, blank=True)

class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=255, blank=True, null=True)
    valor = models.SmallIntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    ordereds = models.ManyToManyField(Ordereds, through='OrderedsTransactions')

class OrderedsTransactions(models.Model):
    id_ordereds = models.ForeignKey(Ordereds, on_delete=models.CASCADE)
    id_transactions = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = [['id_ordereds', 'id_transactions']]
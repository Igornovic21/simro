import uuid

from django.db import models

# Create your models here.
class Marque(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    libelle = models.CharField(max_length=50, default="nom marque", unique=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.libelle


class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    libelle = models.CharField(max_length=50, default="nom produit", unique=True)
    marque = models.ForeignKey(Marque, on_delete=models.CASCADE, related_name="products")
    description = models.TextField(max_length=1000)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.libelle

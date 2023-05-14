from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to = "image/%Y/%m/%d")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name
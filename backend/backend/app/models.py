from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True) 
    price = models.FloatField()  
    stock = models.IntegerField() 

    def clean(self):
        if self.price <= 0:
            raise ValidationError("Price must be positive.")
        if self.stock < 0:
            raise ValidationError("Stock must be zero or greater.")

    def __str__(self):
        return self.name

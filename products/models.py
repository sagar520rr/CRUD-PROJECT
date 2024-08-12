from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    picture = models.ImageField(upload_to='pictures/')  # ImageField to handle images
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

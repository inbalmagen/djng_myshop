from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_deleted = models.BooleanField(default=False)  # Add this field
    
    def __str__(self):
      return f"{self.name} - {self.description} - {self.price}"


class Category(models.Model):
    name = models.CharField(max_length=255)
    popularity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} (Popularity: {self.popularity})"
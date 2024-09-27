from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    popularity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} (Popularity: {self.popularity})"


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_deleted = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category, related_name="products")  # Many-to-many relationship with Category

    def __str__(self):
        return f"{self.name} - {self.description} - {self.price}"

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    owner = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    description = models.TextField()
    pic = models.ImageField( null=True, blank=True)

    def __str__(self):
        return self.name

class NewItem(models.Model):
    new = models.ForeignKey(Item, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return self.name

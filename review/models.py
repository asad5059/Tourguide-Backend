from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class PlaceInfoModel(models.Model):
    TYPE_CHOICES = [
        ('Beach', 'Beach'),
        ('Hill', 'Hill'),
        ('Fountain', 'Fountain'),
        ('Landmark', 'Landmark')
    ]
    owner = models.ForeignKey('auth.User', related_name='review', 
                              on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=300)
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    image = models.ImageField(upload_to='uploads/')
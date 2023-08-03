from django.db import models
from uuid import uuid4
# Create your models here.

class Cars(models.Model):
    id_vehicle = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    model_vehicle = models.CharField(max_length=255)
    manufacturer_vehicle = models.CharField(max_length=255)
    release_year = models.IntegerField()
    status = models.CharField(
        default='N',
        max_length=3,
        choices=(
        ('N','Novo'),
        ('SM', 'Seminovo'),
        ('U', 'Usado')
        )
    )
    description = models.TextField()
    create_at = models.DateField(auto_now_add=True)

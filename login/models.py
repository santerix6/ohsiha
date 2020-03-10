from django.db import models

# Create your models here.
class TestTaulu(models.Model):
    col = models.CharField(max_length=10)

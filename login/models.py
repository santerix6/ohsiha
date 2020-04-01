from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TestTaulu(models.Model):
    pva = models.DateTimeField(default=None)
    sairaanhoitopiiri = models.CharField(max_length=25, default=None,)
    alkuperamaa = models.CharField(max_length=25, default=None)
    alkupera = models.CharField(max_length=100 ,default=None)
    lisaaja = models.ForeignKey(User,default=None, on_delete=models.CASCADE)

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TestTaulu(models.Model):
    pva = models.DateTimeField(default=None)
    potilasid = models.IntegerField(default=None, primary_key = True, )
    sairaanhoitopiiri = models.CharField(max_length=25, default=None, null=True)
    alkuperamaa = models.CharField(max_length=25, default=None, null=True)
    alkupera = models.CharField(max_length=100 ,default=None)
    lisaaja = models.ForeignKey(User,default=None, on_delete=models.CASCADE)

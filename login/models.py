from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TestTaulu(models.Model):
    pva = models.DateField(default=None)
    sairaanhoitopiiri = models.CharField(max_length=25, default=None,)
    alkuperamaa = models.CharField(max_length=25, default=None)
    alkupera = models.ForeignKey('self', default=None, on_delete=models.CASCADE)
    lisaaja = models.ForeignKey(User,default=None, on_delete=models.CASCADE)

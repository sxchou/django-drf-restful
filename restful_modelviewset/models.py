from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(verbose_name='书籍名称', max_length=16)
    price = models.DecimalField(verbose_name='价格', max_digits=8, decimal_places=2)

from django.db import models


# Create your models here.
class Students(models.Model):
    name = models.CharField(verbose_name='学生姓名', max_length=16)
    age = models.IntegerField(verbose_name='年龄')

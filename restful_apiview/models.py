from django.db import models


# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=16)
    password = models.CharField(verbose_name='密码', max_length=16)
    age = models.IntegerField(verbose_name='年龄')


class Author(models.Model):
    name = models.CharField(verbose_name='作者', max_length=16)
    age = models.IntegerField(verbose_name='年龄')

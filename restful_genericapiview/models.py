from django.db import models


# Create your models here.
class Pubilsh(models.Model):
    name = models.CharField(verbose_name='发行商', max_length=16)
    email = models.EmailField(verbose_name='电子邮件', max_length=16)

from django.db import models

class Job_place(models.Model):
    j_place = models.CharField(verbose_name='Организация', max_length=32)
    j_time = models.CharField(verbose_name='Время работы', max_length=32)
    position = models.CharField(verbose_name='Должность', max_length=16)
    resp = models.TextField(verbose_name='Обязанности')


# Create your models here.

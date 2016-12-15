from django.db import models

class Job_place(models.Model):
    j_place = models.CharField(verbose_name='Организация', max_length=128)
    j_time = models.CharField(verbose_name='Время работы', max_length=32)
    position = models.CharField(verbose_name='Должность', max_length=16)
    resp = models.TextField(verbose_name='Обязанности')

class St_place(models.Model):
    st_place = models.CharField(verbose_name='Учебное заведение', max_length=128)
    st_time = models.CharField(verbose_name='Годы обучения', max_length=32)
    department = models.CharField(verbose_name='Факультет', max_length=128)
    specialisation = models.CharField(verbose_name='Специальность', max_length=128)

# Create your models here.

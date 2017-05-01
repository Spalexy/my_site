from django.db import models

class Organisation(models.Model):
    name = models.CharField(verbose_name='Организация', max_length=128)
    region = models.CharField(verbose_name='Регион',max_length=32, blank=True)
    site = models.URLField(verbose_name='Сайт',blank=True)
    phone = models.CharField(verbose_name='Телефон',max_length=16, blank=True)

class Job_place(models.Model):
    j_name = models.ForeignKey(Organisation, verbose_name='Организация', null=True)
    period = models.CharField(verbose_name='Время работы', max_length=16, blank=True)
    position = models.CharField(verbose_name='Должность', max_length=32)
    resp = models.TextField(verbose_name='Обязанности')

class St_place(models.Model):
    st_place = models.CharField(verbose_name='Учебное заведение', max_length=128)
    st_time = models.CharField(verbose_name='Годы обучения', max_length=32)
    department = models.CharField(verbose_name='Факультет', max_length=128)
    specialisation = models.CharField(verbose_name='Специальность', max_length=128)

class Com_card(models.Model):
    j_name = models.ForeignKey(Organisation, verbose_name='Организация', null=True)
    information = models.TextField(verbose_name='О компании')


    

# Create your models here.

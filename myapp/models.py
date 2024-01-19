from django.db import models

# Create your models here.

class Navigation(models.Model):
    title = models.TextField(blank=False, verbose_name='Заголовок вакансии', max_length=25)
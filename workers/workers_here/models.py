from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class Workers(MPTTModel):
    name = models.CharField(max_length = 255, verbose_name = 'ФИО')
    working_place = models.CharField(max_length = 255, verbose_name = 'Должность')
    hire_date = models.DateTimeField(auto_now_add = True, verbose_name = 'Дата приёма на работу')
    salary = models.DecimalField(max_digits = 12, decimal_places = 2, verbose_name = 'Зарплата')
    parent = TreeForeignKey('self', on_delete = models.SET_NULL, null = True, blank = True, related_name = 'children', verbose_name = 'Начальник')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', null = True, blank = True)

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('worker_detailed', kwargs = {'worker_id':self.pk})


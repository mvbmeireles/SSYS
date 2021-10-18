from django.db import models

from datetime import date
from dateutil.relativedelta import relativedelta

class Employee(models.Model):
    name = models.CharField(
        verbose_name='Name',
        max_length=50, null=True,
        blank=True
    )

    email = models.CharField(
        verbose_name='E-mail',
        max_length=50, null=True,
        blank=True
    )

    department = models.CharField(
        verbose_name='Department',
        max_length=20, null=True,
        blank=True
    )

    salary = models.IntegerField(
        verbose_name='Salary',
        null=True, blank=True
    )

    birth_date = models.DateField(
        verbose_name='Birth Date',
        null=True, blank=True
    )

    def age(self):
        try:
            today = date.today()
            time_difference = relativedelta(today, self.birth_date)
            age = time_difference.years
        except:
            age = None
        return age

    def __str__(self):
        return '{}'.format(self.name)
    
    class Meta:
        app_label='employees'
        verbose_name='Employee'
        verbose_name_plural='Employees'
from django.contrib import admin

# Register your models here.

from .models import Employee

@admin.register(Employee)
class CapilarUniversalAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'email',
        'department',
        'salary',
        'birth_date'
    ]

    list_filter = ['name']
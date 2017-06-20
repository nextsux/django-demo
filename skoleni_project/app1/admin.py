from django.contrib import admin
from app1.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'surname')


admin.site.register(Customer, CustomerAdmin)

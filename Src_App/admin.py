from django.contrib import admin
from .models import * 

class Used_Cars_Admin(admin.ModelAdmin):

    list_display = ['title',]
    search_fields = ['title', 'price']

class Services_Admin(admin.ModelAdmin):

    list_display = ['service_name']
    search_fields = ['service_name']

class Time_Admin(admin.ModelAdmin):

    list_display = ['opening_time', 'closing_time']

admin.site.register(Used_Car, Used_Cars_Admin)
admin.site.register(Service, Services_Admin)
admin.site.register(Opening_Hours, Time_Admin)
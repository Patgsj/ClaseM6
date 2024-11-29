from django.contrib import admin

# Register your models here.
from .models import Smartphone

@admin.register(Smartphone)
class SmartphoneAdmin(admin.ModelAdmin):
    list_display = ['model']
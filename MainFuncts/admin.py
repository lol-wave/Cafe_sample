from django.contrib import admin
from .models import Services
# Register your models here.

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'feature_1', 'feature_2', 'feature_3', 'description')

    search_fields = ('name',)
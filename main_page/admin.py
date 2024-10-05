from django.contrib import admin

# Register your models here.
from .models import todo

@admin.register(todo)
class shtoto(admin.ModelAdmin):
    pass

from django.contrib import admin
from .models import Category, Location, Post


admin.site.empty_value_display = 'Не задано'

# Register your models here.
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Post)

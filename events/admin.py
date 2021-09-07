from django.contrib import admin
from .models import Event, Food, Staff, Animal


# Register your models here.

admin.site.register(Event)
admin.site.register(Staff)
admin.site.register(Food)
admin.site.register(Animal)
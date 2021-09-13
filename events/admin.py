from django.contrib import admin
from .models import Event, Food, Staff, Animal, FoodInAnEvent, AnimalInAnEvent


class AdminOnly(admin.ModelAdmin):
    readonly_fields = ('html_content',)


# Register your models here.

admin.site.register(Event, AdminOnly)
admin.site.register(Staff, AdminOnly)
admin.site.register(Food, AdminOnly)
admin.site.register(Animal, AdminOnly)
admin.site.register(FoodInAnEvent, AdminOnly)
admin.site.register(AnimalInAnEvent, AdminOnly)
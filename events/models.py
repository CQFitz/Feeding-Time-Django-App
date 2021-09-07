from django.db import models

# Create your models here.


class Staff(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    staff_name = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.staff_name


class Event(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    event_name = models.CharField(max_length=100, blank=True, default='')
    event_description = models.CharField(max_length=100)
    other_details = models.CharField(max_length=100)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.event_name


class Food(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    food_name = models.CharField(max_length=50, blank=True, default='')

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.food_name


class Animal(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    animal = models.CharField(max_length=60, blank=True, default='')

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.animal


class FoodInAnEvent(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    food_id = models.ForeignKey('Food', on_delete=models.CASCADE)
    event_id = models.ForeignKey('Event', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class AnimalInAnEvent(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    animal_id = models.ForeignKey('Animal', on_delete=models.CASCADE)
    event_id = models.ForeignKey('Event', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
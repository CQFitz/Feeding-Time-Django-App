from django.db import models

# Create your models here.


class Food(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    food_name = models.CharField(max_length=50, blank=True, default='')

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.food_name
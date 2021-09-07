from django.db import models

# Create your models here.


class Animal(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    animal = models.CharField(max_length=60, blank=True, default='')

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.animal
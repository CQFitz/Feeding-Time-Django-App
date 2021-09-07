from django.db import models

# Create your models here.


class Staff(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    staff_name = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.staff_name
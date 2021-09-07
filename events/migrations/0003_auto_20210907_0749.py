# Generated by Django 3.2.6 on 2021-09-07 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_animal_animalinanevent_food_foodinanevent_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animalinanevent',
            name='animal_id',
        ),
        migrations.RemoveField(
            model_name='animalinanevent',
            name='event_id',
        ),
        migrations.RemoveField(
            model_name='foodinanevent',
            name='event_id',
        ),
        migrations.RemoveField(
            model_name='foodinanevent',
            name='food_id',
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
        migrations.DeleteModel(
            name='Animal',
        ),
        migrations.DeleteModel(
            name='AnimalInAnEvent',
        ),
        migrations.DeleteModel(
            name='Food',
        ),
        migrations.DeleteModel(
            name='FoodInAnEvent',
        ),
    ]
# events/serializers
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Event, Staff, Animal, Food


class UserSerializer(serializers.ModelSerializer):
    events = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Event.objects.all()
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'events')


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'event_name', 'event_description', 'other_details')


class StaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staff
        fields = ('id', 'staff_name')


class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = ('id', 'food_name')


class AnimalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Animal
        fields = ('id', 'animal')
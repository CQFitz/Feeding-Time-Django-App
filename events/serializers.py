# events/serializers
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Event, Staff, Animal, Food, FoodInAnEvent, AnimalInAnEvent


class UserSerializer(serializers.HyperlinkedModelSerializer):
    events = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Event.objects.all()
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'events')


class EventSerializer(serializers.HyperlinkedModelSerializer):
    content = serializers.HyperlinkedIdentityField(
        view_name='event-html', format='html')

    class Meta:
        model = Event
        fields = ('url', 'id', 'event_name', 'event_description', 'other_details', 'staff_id', 'content')


class StaffSerializer(serializers.HyperlinkedModelSerializer):
    content = serializers.HyperlinkedIdentityField(
        view_name='staff-html', format='html')

    class Meta:
        model = Staff
        fields = ('url', 'id', 'staff_details', 'content')


class FoodSerializer(serializers.HyperlinkedModelSerializer):
    content = serializers.HyperlinkedIdentityField(
        view_name='food-html', format='html')

    class Meta:
        model = Food
        fields = ('url', 'id', 'food_details', 'content')


class AnimalSerializer(serializers.HyperlinkedModelSerializer):
    content = serializers.HyperlinkedIdentityField(
        view_name='animal-html', format='html')

    class Meta:
        model = Animal
        fields = ('url', 'id', 'animal_details', 'content')


class FoodInAnEventSerializer(serializers.HyperlinkedModelSerializer):
    content = serializers.HyperlinkedIdentityField(
        view_name='food-in-an-event-html', format='html')

    class Meta:
        model = FoodInAnEvent
        fields = ('url', 'id', 'food_id', 'event_id', 'content')


class AnimalInAnEventSerializer(serializers.HyperlinkedModelSerializer):
    content = serializers.HyperlinkedIdentityField(
        view_name='animal-in-an-event-html', format='html')

    class Meta:
        model = AnimalInAnEvent
        fields = ('url', 'id', 'animal_id', 'event_id', 'content')
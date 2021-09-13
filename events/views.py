from django.shortcuts import render
from rest_framework import generics, permissions, renderers
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Event, Staff, Animal, Food, FoodInAnEvent, AnimalInAnEvent
from .serializers import EventSerializer, StaffSerializer, FoodSerializer, AnimalSerializer, FoodInAnEventSerializer, AnimalInAnEventSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'staffs': reverse('staff-list', request=request, format=format),
        'events': reverse('event-list', request=request, format=format),
        'foods': reverse('food-list', request=request, format=format),
        'animals': reverse('animal-list', request=request, format=format),
        'food_in_an_events': reverse('food-in-an-event-list', request=request, format=format),
        'animal_in_an_events': reverse('animal-in-an-event-list', request=request, format=format),
    })

# --- HTML Stuff Start --- #
class StaffHtml(generics.GenericAPIView):
    queryset = Staff.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        staff = self.get_object()
        return Response(staff.html_content)


class EventHtml(generics.GenericAPIView):
    queryset = Event.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        event = self.get_object()
        return Response(event.html_content)


class FoodHtml(generics.GenericAPIView):
    queryset = Food.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        food = self.get_object()
        return Response(food.html_content)


class AnimalHtml(generics.GenericAPIView):
    queryset = Animal.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        animal = self.get_object()
        return Response(animal.html_content)


class FoodInAnEventHtml(generics.GenericAPIView):
    queryset = FoodInAnEvent.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        food_in_an_event = self.get_object()
        return Response(food_in_an_event.html_content)


class AnimalInAnEventHtml(generics.GenericAPIView):
    queryset = AnimalInAnEvent.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        animal_in_an_event = self.get_object()
        return Response(animal_in_an_event.html_content)


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class StaffList(generics.ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class StaffDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class FoodList(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class AnimalList(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class AnimalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class FoodInAnEventList(generics.ListCreateAPIView):
    queryset = FoodInAnEvent.objects.all()
    serializer_class = FoodInAnEventSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class FoodInAnEventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodInAnEvent.objects.all()
    serializer_class = FoodInAnEventSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class AnimalInAnEventList(generics.ListCreateAPIView):
    queryset = AnimalInAnEvent.objects.all()
    serializer_class = AnimalInAnEventSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class AnimalInAnEventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnimalInAnEvent.objects.all()
    serializer_class = AnimalInAnEventSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
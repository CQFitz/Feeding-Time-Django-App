from django.shortcuts import render
from .models import Event
from .serializers import EventSerializer


# Create your views here.

class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializers_class = EventSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializers_class = EventSerializer
from rest_framework import serializers
from .models import Event, Group


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['group', 'name', 'event_datetime', 'place', 'max_attendees']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['name']

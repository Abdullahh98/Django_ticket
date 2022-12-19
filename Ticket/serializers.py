from rest_framework import serializers
from Ticket.models import Tickets, Events

class EventsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['event_id','title', 'city', 'country','image','venue','time','date']

class TicketsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tickets
        fields = ['id', 'user','title','owner','events','price','available','image']


class OrderListSerializer(serializers.ModelSerializer):

    event = EventsListSerializer

    Ticket = TicketsListSerializer(many=True,)

    class Meta:
        model = Tickets
        fields = ['id', 'user','title','owner','events','price','available','image']
class CreateEventsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Events
        fields = ['title', 'city', 'country','image','venue','time','date']
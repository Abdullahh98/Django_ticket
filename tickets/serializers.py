from rest_framework import serializers
from tickets.models import Tickets, Events , Orders
# ...........Events.....................

class EventsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['event_id','title', 'city', 'country','image','venue','time','date']

class EventsUpdateSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Events
        fields = ['event_id','title', 'city', 'country','image','venue','time','date']     


class CreateEventsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Events
        fields = ['event_id','title', 'city', 'country','image','venue','time','date']        

class deleteEventsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Events
        fields = ['event_id','title', 'city', 'country','image','venue','time','date']        


# ............Tickets.....................

class TicketsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tickets
        fields = ['id', 'user','title','owner','events','price','available','image']

class TicketsUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tickets
        fields = ['id', 'user','title','owner','events','price','available','image']


# ............Orders.....................


class OrderListSerializer(serializers.ModelSerializer):

    event = EventsListSerializer

    Ticket = TicketsListSerializer(many=True,)

    class Meta:
        model = Orders
        fields = ['orderseller','order_byuer','ticket_id','current_order','pass_order']
        

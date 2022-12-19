from tickets.models import Orders, Tickets,Events
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView
from tickets.serializers import EventsListSerializer,CreateEventsSerializer, EventsUpdateSerializer
from tickets.serializers import TicketsListSerializer, OrderListSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from tickets.permissions import IsOwner





# ------------- Event VIEWS -------------

class EventListView(ListAPIView):
    serializer_class = EventsListSerializer
    def get_queryset(self):
        queryset = Tickets.objects.all()
        
        return queryset
    permission_classes=[AllowAny]

class EventCreateView(CreateAPIView):
    serializer_class = CreateEventsSerializer
    def perform_create(self, serializer):
        serializer.save()
    permission_classes=[IsAuthenticated]

class EventUpdateView(UpdateAPIView):
    queryset = Events.objects.all()
    serializer_class =  EventsUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'event_id'
    permission_classes = [IsOwner,IsAdminUser]

class EventDeleteView(DestroyAPIView):
    queryset = Events.objects.all()
    serializer_class =CreateEventsSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'event_id'
    permission_classes = [IsOwner,IsAdminUser]


# ------------- Ticket VIEWS -------------

class TicketListView(ListAPIView):
    queryset = Tickets.objects.all()
    serializer_class = TicketsListSerializer
    permission_classes=[AllowAny]

class TicketCreateView(CreateAPIView):
    serializer_class = TicketsListSerializer
    def perform_create(self, serializer):
        serializer.save()
    permission_classes=[IsAuthenticated]

class TicketUpdateView(UpdateAPIView):
    queryset = Tickets.objects.all()
    serializer_class = TicketsListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'ticket_id'
    permission_classes=[IsAuthenticated,IsAdminUser]

class TicketDeleteView(DestroyAPIView):
    queryset = Tickets.objects.all()
    serializer_class = TicketsListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'ticket_id'
    permission_classes=[IsAuthenticated,IsAdminUser]



# ------------- order VIEWS -------------

class OrderListView(ListAPIView):
    serializer_class = OrderListSerializer
    def get_queryset(self):
        Tickets = Orders.objects.all()
        Events = self.request.query_params.get('events')
        if Events is not None:
            Tickets = Events.objects.filter(category__id = Events)
        queryset = Tickets.objects.filter(recipes__in=list(Tickets)).distinct()
        return queryset
    permission_classes=[AllowAny]

class OrderCreateView(CreateAPIView):
    serializer_class = OrderListSerializer
    def perform_create(self, serializer):
        serializer.save()
    permission_classes=[IsAuthenticated]

class OrderUpdateView(UpdateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'ticket_id'
    permission_classes = [IsAuthenticated,IsAdminUser]

class OrderDeleteView(DestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'ticket_id'
    permission_classes=[IsAuthenticated,IsAdminUser]

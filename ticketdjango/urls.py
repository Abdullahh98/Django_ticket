"""ticketdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
from django.contrib import admin
from django.urls import path
from auth.views import UserLoginAPIView, UserCreateAPIView
from Ticket.views import EventListView, EventCreateView, EventUpdateView, EventDeleteView
from Ticket.views import TicketListView, TicketCreateView, TicketUpdateView, TicketDeleteView, OrderListView, OrderCreateView, OrderUpdateView, OrderDeleteView
from auth.views import UserCreateAPIView, UserLoginAPIView
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers



urlpatterns = [
    path('admin/', admin.site.urls),


    # ----- Authentications URLs -----
    path('auth/signup/', UserCreateAPIView.as_view() , name="signup"),
    path('auth/signin/', UserLoginAPIView.as_view() , name="signin"),


    # ----- ticket URLs -----
    path('ticket/', TicketListView.as_view() , name="ticket-list"),
    path('ticket/add/', TicketCreateView.as_view() , name="ticket-add"),
    path('ticket/<int:recipe_id>/edit/', TicketUpdateView.as_view() , name="ticket-edit"),
    path('ticket/<int:recipe_id>/delete/', TicketDeleteView.as_view() , name="ticket-delete"),
    
    
    # ----- events URLs -----
    path('events/', EventListView.as_view() , name="events-list"),
    path('events/add/', EventCreateView.as_view() , name="events-add"),
    path('events/<int:category_id>/edit/', EventUpdateView.as_view() , name="events-edit"),
    path('events/<int:category_id>/delete/', EventDeleteView.as_view() , name="events-delete"),
    
    
    # ----- orders URLs -----
    path('orders/', OrderListView.as_view() , name="order-list"),
    path('orders/add/', OrderCreateView.as_view() , name="order-add"),
    path('orders/<int:ingredient_id>/edit/', OrderUpdateView.as_view() , name="order-edit"),
    path('orders/<int:ingredient_id>/delete/', OrderDeleteView.as_view() , name="order-delete"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

import time
from django.db import models
from django.contrib.auth.models import User
 

class Tickets(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ticketowner")
    title = models.TextField()
    owner = models.TextField()
    events = models.TextField()
    price = models.FloatField()
    available = models.BooleanField()
    image = models.ImageField(help_text='Product Image', upload_to='images', blank=True)


    def __str__(self):
        return f'{self.title, self.owner}'



class Events(models.Model):
    title = models.TextField()
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    image = models.ImageField()
    venue = models.CharField(max_length=50)
    time = models.TimeField()
    date = models.DateField()

def __str__(self):
        return f'{self.title, self.city, self.country, self.venue, self.time, self.date}'
    

class Orders(models.Model):
    order_byuser = models.TextField(max_length=250)
    ticket_id = models.IntegerField()
    def __str__(self):
        return (self.Order_byuser, self.ticket_iD)






from rest_framework.generics import ListAPIView
from rest_framework import serializers
from .models import Flight, Booking


class ListOfFlights(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['id','destination','time','price']


class ListOfBookings(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['flight','date','id']

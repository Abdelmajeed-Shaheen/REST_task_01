from rest_framework.generics import ListAPIView
from .models import Flight, Booking
import datetime
from .serializers import ListOfFlights, ListOfBookings

class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = ListOfFlights


class BookingListView(ListAPIView):
    queryset = Booking.objects.filter(date__gte= datetime.date.today())
    serializer_class = ListOfBookings

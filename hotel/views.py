from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import filters,pagination
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.permissions import BasePermission
from rest_framework.filters import SearchFilter
from django.db.models import Q

class AmenitiesViewset(viewsets.ModelViewSet):
    queryset = models.Amenities.objects.all()
    serializer_class = serializers.AmenitiesSerializer
    
class HotelBookingViewset(viewsets.ModelViewSet):
    queryset = models.HotelBooking.objects.all()
    serializer_class = serializers.HotelBookingSerializer
    
class HotelImagesViewset(viewsets.ModelViewSet):
    queryset = models.HotelImages.objects.all()
    serializer_class = serializers.HotelImagesSerializer


class HotelViewset(viewsets.ModelViewSet):
    queryset = models.Hotel.objects.all()
    serializer_class = serializers.HotelSerializer
    filter_backends = [SearchFilter]
    search_fields = ['hotel_name', 'hotel_price', 'amenities__amenity_name']  # Use amenities__amenity_name

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(hotel_name__icontains=search_query) |  # Search hotel name
                Q(hotel_price__icontains=search_query) |  # Search hotel price
                Q(amenities__amenity_name__icontains=search_query)  # Search related amenity name
            ).distinct()  # Add distinct to avoid duplicates
        return queryset
    
class ReviewViewset(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
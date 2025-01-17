from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import filters,pagination
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.permissions import BasePermission

class AmenitiesViewset(viewsets.ModelViewSet):
    queryset = models.Amenities.objects.all()
    serializer_class = serializers.AmenitiesSerializer
    
class HotelBookingViewset(viewsets.ModelViewSet):
    queryset = models.HotelBooking.objects.all()
    serializer_class = serializers.HotelBookingSerializer
    
class HotelImagesViewset(viewsets.ModelViewSet):
    queryset = models.HotelImages.objects.all()
    serializer_class = serializers.HotelImagesSerializer

class HotelPagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = page_size
    max_page_size = 100
    
class HotelViewset(viewsets.ModelViewSet):
    queryset = models.Hotel.objects.all()
    serializer_class = serializers.HotelSerializer
    pagination_class = HotelPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['hotel_name', 'hotel_price', 'amenity_name']
    
class ReviewViewset(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
from rest_framework import serializers
from . import models

class HotelSerializer(serializers.ModelSerializer):
    amenities = serializers.StringRelatedField(many=True)
    class Meta:
        model = models.Hotel
        fields = '__all__'
        
class AmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Amenities
        fields = '__all__'
        
class HotelImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HotelImages
        fields = '__all__'

class HotelBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HotelBooking
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'
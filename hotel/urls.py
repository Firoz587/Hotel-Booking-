from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() # amader router

router.register('list', views.HotelViewset) # router er antena
router.register('Amenities', views.AmenitiesViewset) # router er antena
router.register('HotelImages', views.HotelImagesViewset) # router er antena
router.register('HotelBooking', views.HotelBookingViewset) # router er antena
router.register('reviews', views.ReviewViewset) # router er antena

urlpatterns = [
    path('', include(router.urls)),
]
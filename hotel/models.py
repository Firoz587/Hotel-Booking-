from django.db import models
from django.contrib.auth.models import User
import uuid


class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4   , editable=False , primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering=['uid']


class Amenities(BaseModel):
    amenity_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.amenity_name
class Hotel(BaseModel):
    hotel_name= models.CharField(max_length=100)
    hotel_price = models.IntegerField()
    description = models.TextField()
    amenities = models.ManyToManyField(Amenities)
    room_count = models.IntegerField(default=10)

    def __str__(self) -> str:
        return self.hotel_name


class HotelImages(BaseModel):
    hotel= models.ForeignKey(Hotel ,related_name="images", on_delete=models.CASCADE)
    images = models.ImageField(upload_to="hotels")
    
    def __str__(self) -> str:
        return self.hotel.hotel_name



class HotelBooking(BaseModel):
    hotel= models.ForeignKey(Hotel  , related_name="hotel_bookings" , on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user_bookings" , on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    booking_type= models.CharField(max_length=100,choices=(('Pre Paid' , 'Pre Paid') , ('Post Paid' , 'Post Paid')))
    
    def __str__(self) -> str:
        return f'{self.hotel.hotel_name} {self.start_date} to {self.end_date}'
    
STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]
class Review(BaseModel):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(choices=STAR_CHOICES, max_length=10)
    
    def __str__(self):
        return f"User : {self.reviewer.first_name} Hotel : {self.hotel.hotel_name}"
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=12)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
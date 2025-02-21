from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12)
    profile_picture = models.ImageField(upload_to='./static/images/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}"

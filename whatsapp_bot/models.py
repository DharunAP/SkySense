from django.db import models
from django.contrib.auth.models import User,AbstractUser

# class CustomUser(AbstractUser):
#     is_whatsapp_enabled = models.BooleanField(default=False)
    
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    latitude=models.CharField(max_length=100)
    longitude=models.CharField(max_length=100)
    landmark=models.CharField(max_length=100,null=True,blank=True)
    phone_no=models.CharField(max_length=15)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    sms_enabled=models.BooleanField(default=0)
    def __str__(self):
        return str(self.user)



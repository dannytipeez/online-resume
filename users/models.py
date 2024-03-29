from email.mime import image
from email.policy import default
from turtle import up
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Skills(models.Model):
    name = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name + ' skill added'


class ChiefImage(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics/Main/")

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"

        def save(self):
            super().save()

            img = Image.open(self.image.path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img = img.save(self.image.path)

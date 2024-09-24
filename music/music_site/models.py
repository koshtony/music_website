from django.db import models

# Create your models here.
class Home(models.Model):
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    
class About(models.Model):
    title = models.CharField(max_lenght=200)
    sub_title = models.CharField(max_length=200)
    content = models.TextField()
    about_image = models.ImageField(default="default.jpg",upload_to="about_images")
    
    
class Events(models.Model):
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(default="default.jpg",upload_to="events_images") 
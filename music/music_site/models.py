from django.db import models

# Create your models here.
class Home(models.Model):
    
    title = models.CharField(max_length=200)
    image = models.ImageField(default="default.jpg",upload_to="home_images")
    content = models.TextField()
    
class About(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    content = models.TextField()
    about_image = models.ImageField(default="default.jpg",upload_to="about_images")
    
    
class EventCategory(models.Model):
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(default="default.jpg",upload_to="events_category_images") 
   
    
class Events(models.Model):
    
    title = models.CharField(max_length=200)
    details = models.TextField(max_length=200)
    location = models.CharField(max_length=200,default="")
    dates = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default="default.jpg",upload_to="events_images")
    
    
class Contacts(models.Model):
    
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    facebook_link = models.URLField(max_length=200)
    insta_link = models.URLField(max_length=200)
    youtube_link = models.URLField(max_length=200)
    location_link = models.TextField(null=True, blank=True)
    address = models.TextField()
    

class item_attributes(models.Model):
    
    attribute = models.CharField(max_length=200)
    description = models.TextField()
    cost = models.FloatField()
    price = models.FloatField()
    status = models.CharField(max_length=200,choices=(('in-stock', 'in-stock'),('low', 'low'),('sold-out', 'sold-out')))
class Items(models.Model):
    
    item_name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    attributes = models.ManyToManyField(item_attributes, blank=True)
    image = models.ImageField(default="default-image", blank=True, upload_to='store_images')
    stage = models.CharField(max_length=200, choices=(('stock', 'stock'),('in-cart', 'in-cart'),('paid', 'paid'),('complete','çomplete'),('returned', 'returned')))
    date = models.DateTimeField()
    
    def __str__(self):
        
        return self.item_name
    
    


    
    

    
    
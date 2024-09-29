from django.db import models
from django.contrib.auth.models import User

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
    
    
class Concerts(models.Model):
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    location  = models.TextField()

    tickets_link = models.TextField()
    concert_cost = models.FloatField(null=True,blank=True)
    concert_returns = models.FloatField(null=True,blank=True)
    poster = models.ImageField(default="default.jpg",upload_to="concert_images")
    date = models.DateTimeField()
    
    
    def __str__(self):
        
        return self.title
    
class Contacts(models.Model):
    
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    facebook_link = models.URLField(max_length=200)
    insta_link = models.URLField(max_length=200)
    youtube_link = models.URLField(max_length=200)
    location_link = models.TextField(null=True, blank=True)
    address = models.TextField()
    
class Blog(models.Model):
    
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now_add=True)
    created_on = models.DateTimeField(auto_now=True)
    blog_image = models.ImageField(default="default.jpg",upload_to="blog_images")
    
    
    def __str__(self):
        return self.title
    
    
    

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
    
    


    
    

    
    
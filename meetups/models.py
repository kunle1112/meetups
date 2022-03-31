from distutils.command import upload
from email.mime import image
from turtle import title
from django.db import models

# Create your models here.


class Location(models.Model):
        name=models.CharField(max_length=50)
        address=models.TextField()
        def __str__(self):
          return f'{self.name}-({self.address})'
    

class Participant(models.Model):
        email=models.EmailField(max_length=254)
        def __str__(self):
            return self.email
        

class Meetup(models.Model):
    organizer_email=models.EmailField(max_length=254)
    title=models.CharField(max_length=200)
    slug=models.SlugField(unique=True)
    description=models.TextField()
    image=models.ImageField(upload_to='images')
    location=models.ForeignKey(Location, on_delete=models.CASCADE)
    participant=models.ManyToManyField(Participant, blank=True)
    
    def __str__(self):
       return f'{self.title}-({self.slug})'
    



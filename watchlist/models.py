from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.

class WatchList(models.Model):
    title = models.CharField(max_length=100)
    storyline = models.TextField(max_length=200)
    active = models.BooleanField(default=True)
    platform=models.ForeignKey('StreamPlatform', on_delete=models.CASCADE, related_name='watchlist')
    avg_rating=models.FloatField(default=0)
    number_rating=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title

class StreamPlatform(models.Model):
    
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=200)
    website = models.URLField(max_length=200)
     
   
    
    def __str__(self):
        return self.name
    
    
class Review(models.Model):
    review_user=models.ForeignKey(User, on_delete=models.CASCADE)
    watchlist=models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name='reviews')
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description=models.CharField(max_length=200, null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    
    
    def __str__(self):
        return str(self.rating) + " | " + self.watchlist.title + " | " +self.review_user.username
    
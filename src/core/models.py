from django.db import models
from django.utils import timezone


class Projects(models.Model):
    title = models.CharField(max_length=100, unique=True)
    link = models.CharField(max_length=300, unique=True)
    poster = models.ImageField(default="poster.jpg", upload_to="site_posters")
    
    def __str__(self) -> str:
        return self.title

class Education(models.Model):
    qualification = models.CharField(max_length=50)
    start_year = models.DateField(auto_now=timezone.now)
    end_year = models.DateField(auto_now=timezone.now)
    description = models.TextField(help_text="give a little about your educational background")


    def __str__(self) -> str:
        return 



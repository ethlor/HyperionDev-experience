from django.db import models
from enum import Enum

# Create your models here.
class TeamChoices(Enum):
    LIV = "Liverpool"
    MAN = "Manchester United"
    CFC = "Chelsea"
    MCTY = "Man City"
    news = "premier league news"


    
class Clubs(models.Model):
    team = models.CharField(max_length=140)
    position = models.IntegerField()
    points = models.IntegerField()

    def __str__(self):
        return self.team
    
 
class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()
    team = models.ForeignKey(Clubs, on_delete=models.CASCADE )

    def __str__(self):
        return self.title



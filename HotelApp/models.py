from distutils.command.upload import upload
import imp
from django.db import models
from django.contrib.auth.models import User
import os




class Collections(models.Model):
    TV = [
        ('y','Yes'),
         ('n','No')
    ]
    CLIMA = [
        ('y','Yes'),
         ('n','No')
    ]
    SHOWER = [
       ('y','Yes'),
         ('n','No')
    ]
    WIFI = [
       ('y','Yes'),
         ('n','No')
    ]
    BALCONY = [
      ('y','Yes'),
         ('n','No')
    ]
    POOL = [
         ('y','Yes'),
         ('n','No')
    ]

    BREAKFAST = [
       ('y','Yes'),
         ('n','No')
    ]
    
    DINNER = [
       ('y','Yes'),
         ('n','No')
    ]
    STARS = [
       (1,'1 Star'),
       (2,'2 Stars'),
       (3,'3 Stars'),
       (4,'4 Stars'),
       (5,'5 Stars'),
       
        
    ]
    
    CollectionName = models.CharField(max_length=30 ,null=False)
    CollectionDescription = models.TextField(null=False)
    Tv= models.CharField(max_length=1 ,null=False,choices=TV)
    Clima= models.CharField(max_length=1 ,null=False,choices=CLIMA)
    Shower= models.CharField(max_length=1 ,null=False,choices=SHOWER)
    Wifi= models.CharField(max_length=1 ,null=False,choices=WIFI)
    Pool= models.CharField(max_length=1 ,null=False,choices=POOL)
    Balcony= models.CharField(max_length=1 ,null=False,choices=BALCONY)
    Breakfast= models.CharField(max_length=1 ,null=False,choices=BREAKFAST)
    Dinner= models.CharField(max_length=1 ,null=False,choices=DINNER)
    KingSize = models.IntegerField(null=False)
    QueenSize = models.IntegerField(null=False)
    SingleSize = models.IntegerField(null=False)
    Stars = models.IntegerField(null=False,choices=STARS)
    price = models.IntegerField(null=False)

    def str(self):
      return str(self.id)
    
    def class_name(self):
      return self.__class__.__name__

    
class Rooms(models.Model):
    RoomNumber = models.IntegerField()
    CollectionId = models.ForeignKey(Collections, on_delete=models.CASCADE)
    RoomImage = models.ImageField(upload_to='images/' ,null=True, blank=True)

    def class_name(self):
      return self.__class__.__name__

class Feedback(models.Model):
    ClientId = models.ForeignKey(User, on_delete=models.CASCADE)
    RoomID = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    FeedbackText = models.TextField()

    def class_name(self):
      return self.__class__.__name__


class Reservations(models.Model):
    ClientId= models.ForeignKey(User, on_delete=models.CASCADE)
    roomId= models.ForeignKey(Rooms, on_delete=models.CASCADE)
    DateD = models.DateField()
    DateF = models.DateField()
    Total = models.FloatField()
    def class_name(self):
      return self.__class__.__name__


class Reservations_History(models.Model):
    ClientId= models.ForeignKey(User, on_delete=models.CASCADE)
    roomId= models.ForeignKey(Rooms, on_delete=models.CASCADE)
    DateD = models.DateField()
    DateF = models.DateField()
    Total = models.FloatField()


    def class_name(self):
      return self.__class__.__name__


from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    city = models.CharField( max_length=50)


class Singer(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)


class Song(models.Model):
    title = models.CharField(max_length=50)
    singer = models.ForeignKey(Singer, related_name='singer', on_delete=models.CASCADE)
    duration = models.DurationField()


    
    
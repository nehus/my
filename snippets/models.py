from __future__ import unicode_literals

from django.db import models




class Userinfo(models.Model):
	uname = models.CharField(max_length=200)
	mobile = models.IntegerField(default=0)
class Temp(models.Model):
	id = models.IntegerField(null=False, blank=True, primary_key=True)
	uname = models.CharField(max_length=200)
	mobile_temp = models.IntegerField(default=0)
	time_temp = models.DateTimeField('date published')	
class Block(models.Model):	
	uname = models.CharField(max_length=200)
	mobile = models.IntegerField(default=0)
	time_active = models.DateTimeField('date published')
class Mobile(models.Model):
	temp= models.ForeignKey(Temp, on_delete=models.CASCADE)
	otp = models.IntegerField(default=0)
	valid_till = models.DateTimeField('date published')	

# Create your models here.

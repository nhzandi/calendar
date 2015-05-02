from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


class numOfYear(models.Model):
	number = models.IntegerField(default=2000, unique=True)

	def __unicode__(self):
		return str(self.number)

class numOfMonth(models.Model):
	numofyear = models.ForeignKey(numOfYear)
	number = models.IntegerField(default=0)	#Number Of the month from 0-11
	name = models.CharField(max_length=15)	#Name of the month:Jan., Feb.,etc.
	numberOfDays = models.IntegerField(default=30)	#This month has 30 days, 31 days,etc.

	def __unicode__(self):
		return self.name

class numOfMonthAdmin(admin.ModelAdmin):
	list_display = ('name', 'numofyear')

class numOfDay(models.Model):
	numofmonth = models.ForeignKey(numOfMonth)
	number = models.IntegerField(default=1)	#Number of the days from 1-31


	def __unicode__(self):
		return str(self.number)

class numOfDayAdmin(admin.ModelAdmin):
	list_display = ('number', 'numofmonth')

class numOfTime(models.Model):
	numofday = models.ForeignKey(numOfDay)
	startHour = models.IntegerField(default=0)	#Hour Time of the day from 0-23
	startMinute = models.IntegerField(default=0)	#Minute Time of the day from 0-59

	def __unicode__(self):
		return str(self.startHour)

class numOfTimeAdmin(admin.ModelAdmin):
	list_display = ('startHour', 'numofday')

class UserProfile(models.Model):
	# This line is required. Links UserProfile to a User model instance.
	user = models.OneToOneField(User)


	# The additional attributes we wish to include.
	website = models.URLField(blank=True, default=None)
#	picture = models.ImageField(upload_to='profile_images', blank=True)

	# Override the __unicode__() method to return out something meaningful!
	def __unicode__(self):
		return self.user.username
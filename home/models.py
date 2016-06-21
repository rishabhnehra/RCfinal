from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils import timezone

class Booking (models.Model):
	first_name = models.CharField(max_length=108)
	last_name = models.CharField(max_length=108)
	email = models.EmailField(max_length=207)
	mobile_number = models.BigIntegerField()
	company = models.CharField(max_length=108)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	appointmentstamp = models.CharField(max_length=108)
	ip_address = models.GenericIPAddressField(protocol='both', unpack_ipv4=False, default='0.0.0.0')
	message = models.TextField(unique=True)
	user_agent = models.CharField(max_length=250, default='No OS')

	def __unicode__(self):
	 	return self.email
	
	# def __str__(self):
	# 	return self.email

class DisabledDates(models.Model):
	id = models.AutoField(primary_key=True)
	disable = models.DateField(unique=True)

	def __unicode__(self):
 		return unicode(self.disable) #This is required to show dates in string

	# def __str__(self):
	# 	return str(	self.disable) #This is required to show dates in string
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models import Avg
import datetime 

import os
import uuid

RATING_CHOICES = (
	(0, 'None'),
	(1, '*'),
	(2, '**'),
	(3, '***'),
	(4, '****'),
	(5, '*****'),
)

YESNO_CHOICES = (
	(0, 'no'),
	(1, 'yes'),
)

def upload_to_location(instance, filename):
    blocks = filename.split('.')
    ext = blocks[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    instance.title = blocks[0]
    return os.path.join('uploads/', filename)

class Locations(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    hours = models.TextField(null=True, blank=True)
    image_file = models.ImageField(upload_to=upload_to_location, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    alcohol = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True)
 
    def __unicode__(self):
        return self.title     

    def get_absolute_url(self):
    	return reverse(viewname="location_list", args=[self.id])

    def get_average_rating(self):
    	average = self.review_set.all().aggregate(Avg('rating'))['rating__avg']
    	if average == None:
    		return average
    	else:
    		return int(average)

    def get_reviews(self):
    	return self.review_set.all()

class Review(models.Model):
	location = models.ForeignKey(Locations)
	user = models.ForeignKey(User)
	description = models.TextField(null=True, blank=True)
	rating = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
	# created_at originally = models.DateTimeField(auto_add_now = True)
	created_at = models.DateTimeField(default=datetime.datetime.now)










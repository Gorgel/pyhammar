from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.
class WallPost(models.Model):
    namn = models.CharField(max_length=120, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    meddelande = models.TextField(max_length=1024, null=False, blank=False)

    def __unicode__(self):
        return smart_unicode(self.namn)

class NewsPost(models.Model):
    headline = models.CharField(max_length=120, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True, auto_now=True)
    body_text = models.TextField(max_length=1024, null=False, blank=False)
    id = models.AutoField(primary_key=True)

    def __unicode__(self):
        return smart_unicode(self.headline)
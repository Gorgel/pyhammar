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

class GolfPost(models.Model):
    headline = models.CharField(max_length=120, null=False, blank=False)
    pub_date = models.DateField()
    body_text = models.TextField(max_length=1024, null=False, blank=False)
    dokument = models.FileField(upload_to='dokument/golf', null=True, blank=True)

    def __unicode__(self):
        return smart_unicode(self.headline)

    class Meta:
        ordering = ('headline',)

class GolfImage(models.Model):
    image = models.ImageField(upload_to='bilder/golfbilder')
    filename = models.CharField(max_length=120, null=False, blank=False)
    caption = models.CharField(max_length=120, null=False, blank=False)
    golf_post = models.ForeignKey(GolfPost)

    def __unicode__(self):
        return smart_unicode(self.filename)

class FiskePost(models.Model):
    headline = models.CharField(max_length=120, null=False, blank=False)
    pub_date = models.DateField()
    body_text = models.TextField(max_length=1024, null=False, blank=False)
    dokument = models.FileField(upload_to='dokument/fiske', null=True, blank=True)

    def __unicode__(self):
        return smart_unicode(self.headline)

    class Meta:
        ordering = ('headline',)

class FiskeImage(models.Model):
    image = models.ImageField(upload_to='bilder/fiskebilder')
    filename = models.CharField(max_length=120, null=False, blank=False)
    caption = models.CharField(max_length=120, null=False, blank=False)
    fiske_post = models.ForeignKey(FiskePost)

    def __unicode__(self):
        return smart_unicode(self.filename)

class FAQPost(models.Model):
    question = models.CharField(max_length=120, null=False, blank=False)
    answer = models.TextField(max_length=512, null=False,blank=False)
    id = models.AutoField(primary_key=True)

    def __unicode__(self):
        return smart_unicode(self.question)

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='galleribilder')
    filename = models.CharField(max_length=120, null=False, blank=False)
    caption = models.CharField(max_length=120, null=False, blank=False)

    def __unicode__(self):
        return smart_unicode(self.filename)







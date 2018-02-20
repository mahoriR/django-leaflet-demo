from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=300)
    lat = models.DecimalField(max_digits=20, decimal_places=6)
    lon = models.DecimalField(max_digits=20, decimal_places=6)
    pages = models.IntegerField(default=1000)
    publish_date = models.DateField()
    website = models.URLField()
    synopsis = models.TextField()
    slug = models.SlugField(max_length=200)
    status = models.BooleanField(default=True)
    #author - model
    #category - m2m?
    #website - URLField
    #sinopsis - Text area
    #slug field - book title
    #status - published / in progress
    #

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/books/{self.id}'
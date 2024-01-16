from django.db import models
class  polls (models.Model):
    title = models.CharField(max_length=200, default="x")
    name = models.CharField(max_length=200,default="x")
    play = models.CharField(max_length=200,default="x")
    play2 = models.URLField(max_length=200,default="x")

class post(models.Model):
    author = models.CharField(max_length=200, default="x")
    title = models.CharField(max_length=200, default="x")
    mood = models.CharField(max_length=200, default="x")
    amount = models.DecimalField(max_digits=10,decimal_places=2,default="2")
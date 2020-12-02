from django.db import models

# Create your models here.
class Places(models.Model):
# class Places:

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    when = models.TextField()
    with_whom = models.TextField()







    # number = int
    # name = str
    # img = str
    # when = str
    # with_whom = str

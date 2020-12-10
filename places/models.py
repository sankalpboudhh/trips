from django.db import models

# Create your models here.
class Places(models.Model):
# class Places:
    class Meta:
        verbose_name_plural = 'places'
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    when = models.TextField()
    with_whom = models.TextField()
    # person = models.ForeignKey(Persons, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
#
# class Category(models.Model):
#     name = models.CharField(max_length=20)
#     class Meta:
#         verbose_name_plural = 'categories'



class Person(models.Model):
    # userid = models.ForeignKey(Places, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    place = models.ForeignKey(Places, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

from django.db import models

# Create your models here.
class Cyber(models.Model):
    name = models.CharField(max_length=22)
    surname = models.CharField(max_length=22)
    email = models.EmailField()
    coments = models.TextField()

    class Meta:
        verbose_name = "IT_Park"
        verbose_name_plural = "IT_Park"

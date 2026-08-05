from django.db import models

# Create your models here.
class Services(models.Model):
    name = models.CharField(max_length=100)
    feature_1 = models.CharField(max_length=80)
    feature_2 = models.CharField(max_length=80)
    feature_3 = models.CharField(max_length=80)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name
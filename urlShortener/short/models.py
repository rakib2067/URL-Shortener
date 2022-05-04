from django.db import models

# Create your models here.


class Url(models.Model):
    urlString = models.CharField(max_length=300, null=False)

    def __str__(self):
        return self.urlString

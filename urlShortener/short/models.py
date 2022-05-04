from django.db import models

# Create your models here.


class Url(models.Model):
    url_string = models.CharField(max_length=300, null=False)
    shortened_url=models.TextField(max_length=100, null=True)

    def __str__(self):
        return f'{self.url_string} {self.shortened_url}'
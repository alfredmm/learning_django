from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
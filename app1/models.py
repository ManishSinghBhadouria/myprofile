from django.db import models

# Create your models here.
class notes(models.Model):
    sname = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resume/', null=True, blank=True)


    def __str__(self):
        return self.sname
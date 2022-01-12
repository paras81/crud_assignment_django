from django.db import models
from django.db.models.deletion import SET_NULL


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class Tasks(models.Model):
    project = models.ForeignKey(Project,on_delete=models.SET_NULL,null=True,blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name
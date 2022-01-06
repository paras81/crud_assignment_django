from django.db.models.deletion import SET_NULL
from django.db import models
from project_management.models import Project

# Create your models here.
class Task(models.Model):
    project = models.ForeignKey(Project,on_delete=models.SET_NULL,null=True,blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name
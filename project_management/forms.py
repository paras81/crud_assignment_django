from django import forms
from django.forms import widgets
from .models import Project, Tasks

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description','duration','image']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.Textarea(attrs={'class': 'form-control'}),

            }
class TasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['project','name', 'description','start_date','end_date']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.Textarea(attrs={'class': 'form-control'}),
            'start_date': widgets.DateInput(attrs={'class': 'form-control', 'type': 'date','placeholder': 'Select a date'}),
            'end_date': widgets.DateInput(attrs={'class': 'form-control', 'type': 'date','placeholder': 'Select a date'}),
            }
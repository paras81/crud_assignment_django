from django import forms
from django.forms import widgets
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['project','name', 'description','start_date','end_date']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.Textarea(attrs={'class': 'form-control'}),

            }
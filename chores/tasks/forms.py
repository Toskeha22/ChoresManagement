from django import forms
from .models import Task, TaskCategory

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title', 'description', 'priority', 'status', 'due_date', 'progress'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Назва завдання'}),
            'description': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Опис завдання','rows': 4}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control',}),
            'progress': forms.NumberInput(attrs={'class': 'form-control','min': 0,'max': 100,})
        }

class TaskCategoryForm(forms.ModelForm):
    class Meta:
        model = TaskCategory
        fields = ['title', 'description', 'color', 'status', 'created_at']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Назва категорії'}),
            'description': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Опис категорії'}),
            'color':  forms.Select(attrs={"class": 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'created_at': forms.DateInput(attrs={'class': 'form-control'})
        }
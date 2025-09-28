from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'category', 'difficulty', 'expected_time', 'periodicity', 'priority']
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть назву завдання'
            }),
            
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Опишіть завдання (необов\'язково)'
            }),
            
            'category': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть категорію'
            }),
            
            'difficulty': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 5,
                'placeholder': 'Від 1 до 5'
            }),
            
            'expected_time': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'год:хв:сек (наприклад: 1:30:00)'
            }),
            
            'periodicity': forms.Select(attrs={
                'class': 'form-select'
            }),
            
            'priority': forms.Select(attrs={
                'class': 'form-select'
            }),
        }
        
        labels = {
            'name': 'Назва завдання',
            'description': 'Опис',
            'category': 'Категорія',
            'difficulty': 'Складність',
            'expected_time': 'Очікуваний час виконання',
            'periodicity': 'Періодичність',
            'priority': 'Пріоритет',
        }



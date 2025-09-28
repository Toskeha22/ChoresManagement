from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Task(models.Model):

    PERIOD_CHOICES = [
            ('once', 'Одноразове'),
            ('daily', 'Щоденне'),
            ('weekly', 'Щотижневе'),
            ('monthly', 'Щомісячне'),
        ]
    PRIORITY_CHOICES = [
        ('low', 'Низький'),
        ('medium', 'Середній'),
        ('high', 'Високий'),
    ]

    name = models.CharField(max_length=200, null=True)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100)
    difficulty = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    expected_time = models.DurationField()
    periodicity = models.CharField(max_length=10, choices=PERIOD_CHOICES, default='once')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    is_archivedd = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta():
        verbose_name = "Завдання"
        verbose_name_plural = "Завдання"

    def __str__(self):
        return self.name


   
  #  МЕТА-ІНФОРМАЦІЯ:
   #     verbose_name = "Завдання"
    #    verbose_name_plural = "Завдання"

  #  МЕТОД str:
   #     ПОВЕРТАЄ значення поля name (для зручного відображення в адмінці)
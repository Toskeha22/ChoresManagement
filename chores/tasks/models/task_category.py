from django.db import models


class TaskCategory(models.Model):
    title = models.CharField(max_length=100, unique=True, blank=True, null=True)
    description = models.TextField(blank=True)
    color = models.CharField(max_length=7, blank=True, default="#007bff")
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name = "Категорія завдань"
        verbose_name_plural = "Категорії завдань"
        ordering = ['-a', '-z']
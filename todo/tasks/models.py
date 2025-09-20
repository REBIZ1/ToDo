import uuid
from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Task(models.Model):
    STATUS_CHOICES = (
    ('todo', 'к исполнению'),
    ('in_progress', 'в процессе'),
    ('done', 'выполнено'),)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')
    status = models.CharField(choices=STATUS_CHOICES, max_length=20, default='todo')
    priority = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=3)
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['owner', 'status']),
            models.Index(fields=['owner', 'priority']),
            models.Index(fields=['due_date']),
        ]
        ordering = ['status', 'priority', 'due_date', '-created_at']

    def __str__(self):
        return f'{self.title} - ({self.get_status_display()})'
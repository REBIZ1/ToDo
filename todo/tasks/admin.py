from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'title', 'status', 'priority', 'due_date')
    list_filter = ('owner', 'status', 'priority')

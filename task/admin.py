from django.contrib import admin
from .models import Task, Priority


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_completed', 'priority', 'due_date', 'created_at')
    list_filter = ('is_completed', 'priority')
    search_fields = ('title', 'description')

@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')
    search_fields = ('name',)

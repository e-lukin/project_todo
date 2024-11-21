from django.db import models

class Priority(models.Model):
    name = models.CharField(
        max_length=50, 
        unique=True, 
        verbose_name="Название приоритета"
        )
    color = models.CharField(
        max_length=7, 
        default="#000000", 
        verbose_name="Цвет приоритета (HEX)"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Приоритет"
        verbose_name_plural = "Приоритеты"
        ordering = ['name']


class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    is_completed = models.BooleanField(default=False, verbose_name="Завершена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    due_date = models.DateField(blank=True, null=True, verbose_name="Крайний срок")
    priority = models.ForeignKey(
        Priority,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Приоритет",
        related_name="tasks"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
        ordering = ['is_completed', 'due_date', '-created_at']

from django.db import models
from django.utils import timezone
import mimetypes


class Group(models.Model):
    name = models.CharField(max_length=55, verbose_name="Название группы")
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name="Дата создания")

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["-date_created"]
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
    

class Elevator(models.Model):
    parent = models.ForeignKey(Group, on_delete=models.SET_NULL, related_name="elevators", blank=True, null=True, verbose_name="Связанная группа")
    name = models.CharField(max_length=55, verbose_name="Название")
    last_connection = models.DateTimeField(blank=True, null=True, verbose_name="Последнее соединение")
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name="Дата создания")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):        
        if not self.pk:
            self.last_connection = timezone.now()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-date_created"]

    class Meta:
        verbose_name = "Лифт"
        verbose_name_plural = "Лифты"


class Advertisement(models.Model):
    parent = models.ForeignKey(Group, on_delete=models.SET_NULL, related_name="advertisements", blank=True, null=True, verbose_name="Связанная группа")
    title = models.CharField(max_length=555, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    ordering = models.IntegerField(default=0, verbose_name="Порядок")
    media = models.FileField(upload_to="admin_A", verbose_name="Реклама")
    filetype = models.CharField(verbose_name="Тип файла:", max_length=50, blank=True)
    duration = models.IntegerField(verbose_name="Продолжительность в секундах:", default=0)
    original_duration = models.IntegerField(verbose_name="Исходная продолжительность в секундах:", default=0)
    size = models.DecimalField(
        max_digits=10,  # Total number of digits
        decimal_places=2,  # Digits after the decimal point
        help_text="Size of the video in megabytes (MB)", 
        default=1
    )
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def save(self, *args, **kwargs):
        if self.media:
            mime_type, _ = mimetypes.guess_type(self.media.name)
            self.filetype = mime_type or 'unknown'
        if self.media and not self.size:
            self.size = round(self.media.size / (1024 * 1024), 2)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Реклама"
        verbose_name_plural = "Реклама"
        ordering = ["-ordering"]